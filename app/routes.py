from flask import render_template, request
from app import app
from app.forms import ApplicationForm
from app.models import Vendor

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/application', methods=['GET', 'POST'])
def application():
    form = ApplicationForm()
    name = form.name
    business = form.business
    address = form.address
    citystatezip = form.citystatezip
    email = form.email
    phoneNum = form.phoneNum
    desc = form.desc
    boothNum = form.boothNum
    tableNum = form.tableNum
    
    if form.is_submitted():
        v = Vendor(name=name, business=business, email=email, address=address, citystatezip=citystatezip, phoneNum=phoneNum, desc=desc, boothNum=boothNum, tableNum=tableNum, )
        result = request.form
        return render_template('index.html', result=result)
    return render_template('application.html', form=form)