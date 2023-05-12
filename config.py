import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'pS^":$j$runAgqGLfCe}/T_`(b-HK'
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    admin_username = "admin"
    admin_password_hash = "bd58bd55b58631402e3946d3909fb325"
    email = 'testemailschool50@gmail.com'
    email_password = 'zktfwkjnfxnnttfk'
    paypal_id = 'AbXgRw_Izf-aLi7jzrJLNYpudep0ZUX69WotOgd4dMDUztgxxMq5QZdLcdMtdKJYnqhvDUNNb-E4qcG3'