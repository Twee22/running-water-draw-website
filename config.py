import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'pS^":$j$runAgqGLfCe}/T_`(b-HK'
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    admin_username = "admin"
    admin_password = "downward-dentist-crisis"
    email = 'testemailschool50@gmail.com'
    email_password = 'zktfwkjnfxnnttfk'