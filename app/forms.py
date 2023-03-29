from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, IntegerField, BooleanField, PasswordField, DateTimeField
from wtforms.validators import InputRequired, Length, NumberRange, DataRequired, ValidationError


class ApplicationForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()], render_kw={"placeholder": "Your Name Here"})
    business = StringField('Business Name', validators=[InputRequired()], render_kw={"placeholder": "Business Name Here"})
    address = StringField('Address', validators=[InputRequired()], render_kw={"placeholder": "Address Here"})
    citystatezip = StringField('City, State, Zip', validators=[InputRequired()], render_kw={"placeholder": "City, State, and Zip"})
    email = EmailField('Email Address', validators=[InputRequired()], render_kw={"placeholder": "Email Here"})
    phoneNum = StringField('Phone Number', validators=[InputRequired()], render_kw={"placeholder": "Phone Number Here"})
    desc = StringField('Description of Sales Items', validators=[InputRequired()], render_kw={"placeholder": "Write a Description of What Your Business Does Here"})
    boothNum = IntegerField('Number of Booths', validators=[InputRequired(), NumberRange(min=1,max=4)])
    boothLoc = StringField('Booth Location(s)', validators=[InputRequired()], render_kw={"placeholder": "Booth Location(s) here"})
    tableNum = IntegerField('Number of Tables', validators=[InputRequired(), NumberRange(min=0, max=20)])
    date = DateTimeField('Date and Time', format='%Y/%m/%d %H:%M:%S')
    terms = BooleanField('I have read and agree to this', validators=[InputRequired()])
    sign = StringField('Signed', validators=[InputRequired()])
    submit = SubmitField('Next')



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "username"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "password"})
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')