from flask import Flask, render_template, url_for, request
from app.forms import ApplicationForm
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/application')
def application():
    form = ApplicationForm()
    return render_template('application.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)

