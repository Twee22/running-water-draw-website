from flask import render_template
from app import app

@app.route('/')
@app.route('/temp_index')
def index():
    return render_template('temp_index.html')