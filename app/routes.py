from flask import render_template, request
from app import app
from app.forms import ApplicationForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/application')
def application():
    form = ApplicationForm()
    return render_template('application.html', form=form)