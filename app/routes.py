from flask import render_template, request, redirect, url_for, session, send_file, flash, send_from_directory
from flask_login import login_required, current_user, login_user, logout_user
from app import app, db, ckeditor
from app.forms import ApplicationForm, LoginForm, AdminForm, AdminApplicationForm, AdminEditForm
from app.models import Vendor, User, AppText, CurrentYear
from app.vendor_dict import update
from app.payment_deadline import save_initial_time, check_db, future_times, set_deadline, get_deadline, get_booth_price, payment_deadline_days
from app.send_email import send_email, send_payment_confirmation_email, send_decline_email, application_recieved
import csv, os, datetime
from config import Config

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    # gets directory of folder holding images and passes it to index
    image_names= os.listdir("./app/static/carousel")
    #test_vendors = [{'name': 'Melanie Kohn', 'business': 'Celebrity', 
    #               'desc': 'Voice of Lucy Van Pelt', 'boothNum': '41'},
    #               {'name': 'Duncan Watson', 'business': 'Celebrity', 
    #               'desc': 'Voice of Charlie Brown', 'boothNum': '42'}]

    # Adds a hi to notes in the database so that it can be edited
    #a = AppText(notes = 'hi')
    #b = CurrentYear(year = 2023)
    #db.session.add(a)
    #db.session.add(b)
    #db.session.commit()

    vendors = Vendor.query.order_by(Vendor.boothNum)
    check_db(vendors)
    currYear = CurrentYear.query.first().year
    vendor_dict = update(vendors, current_year = currYear)
    
    return render_template('index.html', image_name = image_names, vendors = vendors, vendor_dict = vendor_dict, current_year=currYear)

@app.route('/info')
def info():
    boothLoc = request.args.get('booth_num')
    session['boothLoc_'] = boothLoc
    return redirect(url_for('application'))

@app.route('/application', methods=['GET', 'POST'])  # create route for application page
def application():
    form = ApplicationForm()  # create instance of application form
    appText = AppText.query.first()  # get application text from database
    boothLoc_ = session.get('boothLoc_', None)  # get booth location from session

    currYear = CurrentYear.query.first().year  # get current year from database
    vendors = Vendor.query.order_by(Vendor.boothNum)  # get list of vendors from database
    vendor_dict = update(vendors, current_year=currYear)  # create dictionary of vendors with booth info

    if form.validate_on_submit():  
        # if form submitted and validated
        deadline_date = session.get('deadline_date')
        if deadline_date is None:
            deadline_date = datetime.datetime(currYear, 8, 1).date()
        else:
            deadline_date = datetime.datetime.strptime(deadline_date.strftime('%Y-%m-%d'), '%Y-%m-%d').date()   # Convert date to string and then to datetime object
        boothPrice = get_booth_price(form, deadline_date)
        # get booth price based on form data and deadline

        #deadline_date = datetime.datetime(currYear, 8, 1).date()  # get deadline date for payment
        
        v = Vendor(name=form.name.data, business=form.business.data, address=form.address.data,
                   citystatezip=form.citystatezip.data, email=form.email.data, phoneNum=form.phoneNum.data,
                   desc=form.desc.data,
                   boothNum=form.boothNum.data, boothLoc=form.boothLoc.data, tableNum=form.tableNum.data,
                   date=form.date.data, status="pendingApproval",
                   payment_amount=(10 * form.tableNum.data) + int(boothPrice), year=currYear)  # create vendor instance with form data

        db.session.add(v)  # add vendor to database session
        db.session.commit()  # commit changes to database
        # save vendor data in session
        session['name'] = str(v.name)
        session['business'] = str(v.business)
        session['address'] = str(v.address)
        session['citystatezip'] = str(v.citystatezip)
        session['email'] = str(v.email)
        session['phoneNum'] = str(v.phoneNum)
        session['desc'] = str(v.desc)
        session['boothNum'] = str(v.boothNum)
        session['boothLoc'] = str(v.boothLoc)
        session['tableNum'] = str(v.tableNum)
        session['date'] = str(v.date)
        application_recieved(v)
        return redirect('/confirmation')  # redirect to confirmation page if successful submission

    return render_template('application.html', form=form, appText=appText, boothLoc_=boothLoc_,
                           vendor_dict=vendor_dict)  # render application template with form data and vendor info

@app.route('/set_cutoff', methods=['POST'])
def set_cutoff():
    deadline_date = request.form['deadline_date']
    session['deadline_date'] = deadline_date
    return redirect(url_for('adminapp'))

@app.route('/update_pricing', methods=['POST'])
def update_pricing():
    one_booth_price = request.form['one_booth']
    two_booths_price = request.form['two_booths']
    one_booth_post_cutoff_price = request.form['one_booth_post_cutoff']
    two_booths_post_cutoff_price = request.form['two_booths_post_cutoff']
    session['one_booth_price'] = one_booth_price
    session['two_booths_price'] = two_booths_price
    session['one_booth_post_cutoff_price'] = one_booth_post_cutoff_price
    session['two_booths_post_cutoff_price'] = two_booths_post_cutoff_price
    return redirect(url_for('adminapp'))


# Define a Flask route for the confirmation page
@app.route('/confirmation')
def confirmation():
    # Retrieve the data stored in the session variable for each variable
    name = session.get('name')                      # Get the user's name
    business = session.get('business')              # Get the user's business name
    address = session.get('address')                # Get the user's address
    citystatezip = session.get('citystatezip')      # Get the user's city, state, and ZIP code
    email = session.get('email')                    # Get the user's email address
    phoneNum = session.get('phoneNum')              # Get the user's phone number
    desc = session.get('desc')                      # Get the user's description of their business
    boothNum = session.get('boothNum')              # Get the user's booth number
    boothLoc = session.get('boothLoc')              # Get the user's booth location
    tableNum = session.get('tableNum')              # Get the user's table number
    date = session.get('date')                      # Get the user's preferred date for the event

    # Render the confirmation.html template with the retrieved data
    return render_template('confirmation.html', name=name, business=business, address=address, citystatezip=citystatezip, email=email, phoneNum=phoneNum,
                           desc=desc, boothNum=boothNum, boothLoc=boothLoc, tableNum=tableNum, date=date)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Create a login form
    form = LoginForm()

    # If the form is submitted and valid
    if form.validate_on_submit():
        # Check if the user is the admin and redirect to adminapp if true
        if (form.username.data == Config.admin_username and form.password.data == Config.admin_password):
            return redirect(url_for('adminapp'))
        # Otherwise, try to find the user in the database and authenticate them
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            # Redirect back to the login page if authentication fails
            return redirect(url_for('login'))
        # Log in the user and redirect to the index page
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    # Render the login page with the form
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    # Log out the user
    logout_user()
    # Render the index page
    return render_template('index.html')

@app.route('/adminapp', methods=['GET', 'POST'])
def adminapp():
    form = AdminForm()
    data = Vendor.query.all()
    appData = AppText.query.first()
    currYear = CurrentYear.query.first()

    # Check if the payment deadline is already set in the session
    deadline = session.get('deadline', get_deadline())

    if request.method == 'POST':
        if 'currYearBtn' in request.form:
            # Handle current year update
            try:
                new_year = request.form['year']
                current_year = CurrentYear.query.first()
                current_year.year = new_year
                db.session.commit()
            except:
                pass
        elif 'paymentDeadlineBtn' in request.form:
            # Handle payment deadline update
            try:
                new_deadline = int(request.form['day'])
                set_deadline(new_deadline)
                # Store the new deadline in the session
                session['deadline'] = new_deadline
                deadline = new_deadline

                # Update payment_deadline for all vendors with new deadline
                vendors = Vendor.query.all()
                for vendor in vendors:
                    vendor.payment_deadline = future_times()
                db.session.commit()

            except:
                pass

    return render_template('AdminApp.html', data=data, form=form, appData=appData, current_year=currYear.year, deadline=deadline)



# Define a route for the admin app that takes an integer parameter called id and supports GET and POST requests
@app.route('/adminapp/<int:id>', methods=['GET', 'POST'])
def adminappupdate(id):
    # Retrieve the Vendor object with the specified id, or return a 404 error if not found
    vendor_status_update = vendor_payment_deadline = Vendor.query.get_or_404(id)
    
    # If the request method is POST, process the form data
    if request.method == 'POST':
        # Get the values of the 'email' and 'action' fields from the submitted form data
        email = request.form['action']
        action = request.form['action']
        
        # If the 'email' field is set to 'send_email', send an email to the vendor
        if email == 'send_email':
            send_email(vendor_status_update)
        
        # If the 'action' field is set to 'confirm', update the vendor status to 'pendingPayment'
        # and set the payment deadline to a future time
        if action == 'confirm':
            vendor_status_update.status = 'pendingPayment'
            send_email(vendor_status_update)
            if vendor_status_update.status == 'pendingPayment':
                vendor_payment_deadline.date == save_initial_time()
                vendor_payment_deadline.payment_deadline = future_times()
        
        # If the 'action' field is set to 'deny', update the vendor status to 'denied'
        elif action == 'deny':
            vendor_status_update.status = 'denied'
            send_decline_email(vendor_status_update)
        
        # Commit the changes to the database and display a success message
        while True:
            try:
                db.session.commit()
                flash('Vendor status updated successfully!', 'success')
                break
            # If there is an exception while committing the changes, return an error message
            except Exception as e:
                print(e)
                return "There was a problem updating the status of the vendor"
        
        # Redirect the user to the adminapp page
        return redirect(url_for('adminapp'))
    
    # If the request method is GET, render the adminapp page
    elif request.method == 'GET':
        return render_template(url_for('adminapp'))

    
@login_required # This decorator ensures that only logged-in users can access this page
@app.route('/adminDB', methods=['GET', 'POST'])
def adminDB():
    form = AdminApplicationForm()
    if form.validate_on_submit():
        currYear = CurrentYear.query.first().year # Get the current year from the database
        v = Vendor(name = form.name.data, business = form.business.data, address = form.address.data, 
                   citystatezip = form.citystatezip.data, email = form.email.data, phoneNum = form.phoneNum.data, desc = form.desc.data, 
                   boothNum = form.boothNum.data, boothLoc = form.boothLoc.data, tableNum = form.tableNum.data, date = form.date.data, status="pendingApproval",
                   payment_amount = form.payment_amount.data, year=currYear)
        
        db.session.add(v)  # Add the new vendor to the database
        db.session.commit()  # Commit the changes to the database
        return redirect(url_for('adminapp'))  # Redirect to the adminapp page
    return render_template('adminDB.html', form=form)  # Render the adminDB.html template with the form object

@app.route('/DBEdit/<int:id>', methods=['GET', 'POST'])
def DBEdit(id):
    # Get the vendor object with the specified ID or return a 404 error if not found
    vendor = Vendor.query.get_or_404(id)
    # Create a new AdminEditForm and pre-populate it with the data from the vendor object
    form = AdminEditForm(obj=vendor)
    
    # If the form has been submitted and passes validation...
    if form.validate_on_submit():
        # Update the vendor object with the data from the form
        form.populate_obj(vendor)
        # Commit the changes to the database
        db.session.commit()
        # Flash a success message to the user
        flash('Vendor has been updated', 'success')
        # Redirect the user to the adminapp page
        return redirect(url_for('adminapp'))
    else:
        # If the form has not been submitted or does not pass validation, print any errors to the console
        print(form.errors)
    # Render the DBEdit.html template, passing in the form and vendor objects
    return render_template('DBEdit.html', form=form, vendor=vendor)


    
# This route is used to download data from the database as a CSV file
# The route can only be accessed by an admin user
@app.route('/adminapp/download_data')
def admin_download_data():

    # Open a new CSV file to write the data to
    with open('database_dump.csv', 'w', newline='') as csv_file:
        # Use the CSV writer to write the data to the file
        wr = csv.writer(csv_file, delimiter=",")
        # Get all the Vendor records from the database
        records = Vendor.query.all()
        # Write the header row to the CSV file
        wr.writerow(list(filter(None,[ i[0] if (not i[0].startswith('_') and not i[0] == "followers") else None for i in Vendor.__dict__.items()])))
        # Write the data for each record to the CSV file
        for r in records:
            wr.writerow(r)
            
    # Return the CSV file as a downloadable attachment
    return send_file(
        '../database_dump.csv',
        mimetype='text/csv',
        download_name='Vendor_List.csv',
        as_attachment=True
    )


# Payment confirmation page
@app.route('/payment/<int:id>', methods=['POST', 'GET'])
def payment(id):
    # Get the vendor object from the database based on the ID
    vendor_status_update = Vendor.query.get_or_404(id)
    # Render the PaymentConfirmation.html template and pass in the vendor object
    return render_template('PaymentConfirmation.html', vendor=vendor_status_update)

# Payment capture route
@app.route('/payments/<int:id>/capture', methods=['POST', 'GET'])
def payment_capture(id):
    # Get the vendor object from the database based on the ID
    vendor_status_update = Vendor.query.get_or_404(id)
    if request.method == 'POST':
        # If the request method is POST, update the vendor's status to 'finalized'
        vendor_status_update.status = 'finalized'
        # Send a payment confirmation email to the vendor
        send_payment_confirmation_email(vendor_status_update)
        while True:
            try:
                # Attempt to commit the changes to the database
                db.session.commit()
                break
            except:
                # If there is an error, return an error message
                return "There was a problem updating the status of the vendor"
        # Render the PaymentConfirmation.html template and pass in the vendor object
        return render_template('PaymentConfirmation.html', vendor=vendor_status_update)
    elif request.method == 'GET':
        # If the request method is GET, simply render the PaymentConfirmation.html template and pass in the vendor object
        return render_template('PaymentConfirmation.html', vendor=vendor_status_update)
