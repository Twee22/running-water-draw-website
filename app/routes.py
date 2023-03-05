from flask import render_template, request
from app import app, db
from app.forms import ApplicationForm
from app.models import Vendor
import os

@app.route('/')
@app.route('/index', methods=['POST'])
def index():
    # gets directory of folder holding images and passes it to index
    image_names= os.listdir("./app/static/carousel")
    return render_template('index.html', image_name = image_names)

@app.route('/application', methods=['GET', 'POST'])
def application():
    form = ApplicationForm()
        
    print("Gets here")
    if form.validate_on_submit():
        print("Gets here 2")
        v = Vendor(name = form.name.data, business = form.business.data, address = form.address.data, citystatezip = form.citystatezip.data, email = form.email.data, phoneNum = form.phoneNum.data, desc = form.desc.data, boothNum = form.boothNum.data, tableNum = form.tableNum.data)
        db.session.add(v)
        db.session.commit()
        return render_template('index.html')
    return render_template('application.html', form=form)
