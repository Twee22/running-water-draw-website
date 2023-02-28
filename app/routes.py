from flask import render_template, request
from app import app
from app.forms import ApplicationForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/application', methods=['GET', 'POST'])
def application():
    form = ApplicationForm()
    if form.is_submitted():
        result = request.form
        return render_template('index.html', result=result)
    return render_template('application.html', form=form)