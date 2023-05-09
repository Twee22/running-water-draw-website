from flask import render_template, request, redirect, url_for, session, send_file, flash, send_from_directory
from flask_login import login_required, current_user, login_user, logout_user
from app import app, db, ckeditor
from app.forms import ApplicationForm, LoginForm, AdminForm, AdminApplicationForm, AdminEditForm
from app.models import Vendor, User, AppText, CurrentYear
from app.vendor_dict import update
from app.payment_deadline import save_initial_time, check_db, future_times, set_deadline, get_deadline, payment_deadline_days
from app.send_email import send_email, send_payment_confirmation_email, send_decline_email
import csv, os
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

@app.route('/application', methods=['GET', 'POST'])
def application():
    form = ApplicationForm()
    appText = AppText.query.first()
    boothLoc_ = session.get('boothLoc_', None)
    
    currYear = CurrentYear.query.first().year
    vendors = Vendor.query.order_by(Vendor.boothNum)
    vendor_dict = update(vendors, current_year=currYear)
    
    if form.validate_on_submit():
        if form.boothNum.data == 1:
            boothPrice = 150
        else:
            boothPrice = 200


        v = Vendor(name = form.name.data, business = form.business.data, address = form.address.data, 
                   citystatezip = form.citystatezip.data, email = form.email.data, phoneNum = form.phoneNum.data, desc = form.desc.data, 
                   boothNum = form.boothNum.data, boothLoc = form.boothLoc.data, tableNum = form.tableNum.data, date = form.date.data, status="pendingApproval",
                   payment_amount = (10 * form.tableNum.data) + boothPrice, year=currYear)
        db.session.add(v)
        db.session.commit()
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
        return redirect('/confirmation')
    return render_template('application.html', form=form, appText=appText, boothLoc_ = boothLoc_, vendor_dict = vendor_dict)

@app.route('/confirmation')
def confirmation():
    # Retrieve the data stored in the session variable
    name = session.get('name')
    business = session.get('business')
    address = session.get('address')
    citystatezip = session.get('citystatezip')
    email = session.get('email')
    phoneNum = session.get('phoneNum')
    desc = session.get('desc')
    boothNum = session.get('boothNum')
    boothLoc = session.get('boothLoc')
    tableNum = session.get('tableNum')
    date = session.get('date')

    return render_template('confirmation.html', name=name, business=business, address=address, citystatezip=citystatezip, email=email, phoneNum=phoneNum,
                           desc=desc, boothNum=boothNum, boothLoc=boothLoc, tableNum=tableNum, date=date)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if (form.username.data == Config.admin_username and form.password.data == Config.admin_password):
            return redirect(url_for('adminapp'))
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
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

    
@login_required
@app.route('/adminDB', methods=['GET', 'POST'])
def adminDB():
    form = AdminApplicationForm()
    if form.validate_on_submit():
        currYear = CurrentYear.query.first().year
        v = Vendor(name = form.name.data, business = form.business.data, address = form.address.data, 
                   citystatezip = form.citystatezip.data, email = form.email.data, phoneNum = form.phoneNum.data, desc = form.desc.data, 
                   boothNum = form.boothNum.data, boothLoc = form.boothLoc.data, tableNum = form.tableNum.data, date = form.date.data, status="pendingApproval",
                   payment_amount = form.payment_amount.data, year=currYear)
        db.session.add(v)
        db.session.commit()
        return redirect(url_for('adminapp'))
    return render_template('adminDB.html', form=form)

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


    
@app.route('/adminapp/download_data')
def admin_download_data():

    with open('database_dump.csv', 'w', newline='') as csv_file:
        wr = csv.writer(csv_file, delimiter=",")
        records = Vendor.query.all()
        wr.writerow(list(filter(None,[ i[0] if (not i[0].startswith('_') and not i[0] == "followers") else None for i in Vendor.__dict__.items()])))
        for r in records:
            wr.writerow(r)
            
    return send_file(
        '../database_dump.csv',
        mimetype='text/csv',
        download_name='Vendor_List.csv',
        as_attachment=True
    )

@app.route('/payment/<int:id>', methods=['POST', 'GET'])
def payment(id):
    vendor_status_update = Vendor.query.get_or_404(id)
    return render_template('PaymentConfirmation.html', vendor=vendor_status_update)

    
@app.route('/payments/<int:id>/capture', methods=['POST', 'GET'])
def payment_capture(id):
    vendor_status_update = Vendor.query.get_or_404(id)
    if request.method == 'POST':
        vendor_status_update.status = 'finalized'
        send_payment_confirmation_email(vendor_status_update)
        while True:
            try:
                db.session.commit()
                break
            except:
                return "There was a problem updating the status of the vendor"
        return render_template('PaymentConfirmation.html', vendor=vendor_status_update)
    elif request.method == 'GET':
        return render_template('PaymentConfirmation.html', vendor=vendor_status_update)