from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app import app, db
from app.forms import ApplicationForm, LoginForm
from app.models import Vendor, User

@app.route('/')
@app.route('/index', methods=['POST'])
def index():
    return render_template('index.html')

@app.route('/application', methods=['GET', 'POST'])
def application():
    form = ApplicationForm()
        
    if form.validate_on_submit():
        v = Vendor(name = form.name.data, business = form.business.data, address = form.address.data, citystatezip = form.citystatezip.data, email = form.email.data, phoneNum = form.phoneNum.data, desc = form.desc.data, boothNum = form.boothNum.data, tableNum = form.tableNum.data)
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