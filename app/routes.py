from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app import app, db
from app.forms import ApplicationForm, LoginForm
from app.models import Vendor, User

import os

@app.route('/')
@app.route('/index', methods=['POST'])
def index():
    # gets directory of folder holding images and passes it to index
    image_names= os.listdir("./app/static/carousel")
    #test_vendors = [{'name': 'Melanie Kohn', 'business': 'Celebrity', 
    #               'desc': 'Voice of Lucy Van Pelt', 'boothNum': '41'},
    #               {'name': 'Duncan Watson', 'business': 'Celebrity', 
    #               'desc': 'Voice of Charlie Brown', 'boothNum': '42'}]
    vendors = Vendor.query.order_by(Vendor.boothNum)
    return render_template('index.html', image_name = image_names, vendors = vendors)

@app.route('/application', methods=['GET', 'POST'])
def application():
    form = ApplicationForm()
        
    if form.validate_on_submit():
        v = Vendor(name = form.name.data, business = form.business.data, address = form.address.data, 
                   citystatezip = form.citystatezip.data, email = form.email.data, phoneNum = form.phoneNum.data, desc = form.desc.data, 
                   boothNum = form.boothNum.data, tableNum = form.tableNum.data, date = form.date.data, status="pendingApproval")
        db.session.add(v)
        db.session.commit()
        return render_template('index.html')
    return render_template('application.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return render_template('index.html')

@app.route('/adminapp', methods=['POST', 'GET'])
def adminapp():
    
    return render_template('AdminApp.html')

@app.route('/adminapp/<int:id>', methods=['POST', 'GET'])
def adminapp(id):
    if request.method == 'POST':
        vendor_status_update = Vendor.query.get_or_404(id)
        if request.form.get('confirm') == 'confirm':
            vendor_status_update.status = "pendingPayment"
        elif  request.form.get('deny') == 'deny':
            vendor_status_update.status = "denied"
        else:
            pass
        try:
            db.session.commit()
            return render_template('AdminApp.html', vendor_status_update=vendor_status_update)
        except:
            return "There was a problem updating the status of the vendor"

    elif request.method == 'GET':
        return render_template('AdminApp.html')
