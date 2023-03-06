from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, IntegerField, BooleanField, PasswordField
from wtforms.validators import InputRequired, Length, NumberRange, DataRequired

class ApplicationForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    business = StringField('Business Name', validators=[InputRequired()])
    address = StringField('Address', validators=[InputRequired()])
    citystatezip = StringField('City, State, Zip', validators=[InputRequired()])
    email = EmailField('Email Address', validators=[InputRequired()])
    phoneNum = StringField('Phone Number', validators=[InputRequired()])
    desc = StringField('Description of Sales Items', validators=[InputRequired()])
    boothNum = IntegerField('Number of Booths', validators=[InputRequired(), NumberRange(min=1,max=4)])
    tableNum = IntegerField('Number of Tables', validators=[InputRequired(), NumberRange(min=0, max=20)])
    terms = BooleanField('I have read and agree to this', validators=[InputRequired()])
    sign = StringField('Signed', validators=[InputRequired()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')