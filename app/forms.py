from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, IntegerField, BooleanField, PasswordField, DateTimeField, FloatField, SelectField
from wtforms.validators import InputRequired, Length, NumberRange, DataRequired, ValidationError
from flask_ckeditor import CKEditorField
from datetime import datetime, timezone
from app.map_contraints import validate_boothLoc, validate_boothLoc_admin, validate_boothNum_loc_match, validate_boothLoc_available,  validate_no_digits, validate_phoneNum, validate_no_special_chars
import pytz

class ApplicationForm(FlaskForm):    
    name = StringField('Name', validators=[InputRequired(), validate_no_digits, validate_no_special_chars], render_kw={"placeholder": "Your Full Name Here"})
    business = StringField('Business Name', validators=[InputRequired()], render_kw={"placeholder": "Business Name Here"})
    address = StringField('Address', validators=[InputRequired()], render_kw={"placeholder": "Address Here"})
    citystatezip = StringField('City, State, Zip', validators=[InputRequired()], render_kw={"placeholder": "City, State, and Zip"})
    email = EmailField('Email Address', validators=[InputRequired()], render_kw={"placeholder": "Email Here"})
    phoneNum = StringField('Phone Number', validators=[InputRequired(), validate_phoneNum], render_kw={"placeholder": "Phone Number Here"})
    desc = StringField('Description of Sales Items', validators=[InputRequired()], render_kw={"placeholder": "Write a Description of What Your Business Does Here"})
    boothNum = IntegerField('Number of Booths', validators=[InputRequired(), validate_boothNum_loc_match, NumberRange(min=1,max=4)])
    boothLoc = StringField('Booth Location(s)', validators=[InputRequired(), validate_boothLoc, validate_boothLoc_available], render_kw={"placeholder": "Booth Location(s) here"})
    tableNum = IntegerField('Number of Tables', validators=[InputRequired(), NumberRange(min=0, max=20)])
    date = DateTimeField('Date and Time', format='%H:%M:%S %m-%d-%Y', default=datetime.strptime(datetime.now(pytz.timezone('US/Central')).strftime('%H:%M:%S %m-%d-%Y'), '%H:%M:%S %m-%d-%Y'))
    terms = BooleanField('I have read and agree to this', validators=[InputRequired()])
    #sign = StringField('Signed', validators=[InputRequired()])
    submit = SubmitField('Submit')

class AdminApplicationForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), validate_no_digits], render_kw={"placeholder": "Your Full Name Here"})
    business = StringField('Business Name', validators=[InputRequired()], render_kw={"placeholder": "Business Name Here"})
    address = StringField('Address', validators=[InputRequired()], render_kw={"placeholder": "Address Here"})
    citystatezip = StringField('City, State, Zip', validators=[InputRequired()], render_kw={"placeholder": "City, State, and Zip"})
    email = EmailField('Email Address', validators=[InputRequired()], render_kw={"placeholder": "Email Here"})
    phoneNum = StringField('Phone Number', validators=[InputRequired()], render_kw={"placeholder": "Phone Number Here"})
    desc = StringField('Description of Sales Items', validators=[InputRequired()], render_kw={"placeholder": "Write a Description of What Your Business Does Here"})
    boothNum = IntegerField('Number of Booths', validators=[InputRequired(), validate_boothNum_loc_match])
    boothLoc = StringField('Booth Location(s)', validators=[InputRequired(), validate_boothLoc_admin, validate_boothLoc_available], render_kw={"placeholder": "Booth Location(s) here"})
    tableNum = IntegerField('Number of Tables', validators=[InputRequired(), NumberRange(min=0, max=20)])
    date = DateTimeField('Date and Time', format='%H:%M:%S %m-%d-%Y', default=datetime.strptime(datetime.now(pytz.timezone('US/Central')).strftime('%H:%M:%S %m-%d-%Y'), '%H:%M:%S %m-%d-%Y'))
    payment_amount = FloatField('Payment Amount', render_kw={"placeholder": "Payment Amount Here"})
    submit = SubmitField('Submit')

class AdminEditForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), validate_no_digits], render_kw={"placeholder": "Your Full Name Here"})
    business = StringField('Business Name', validators=[InputRequired()], render_kw={"placeholder": "Business Name Here"})
    address = StringField('Address', validators=[InputRequired()], render_kw={"placeholder": "Address Here"})
    citystatezip = StringField('City, State, Zip', validators=[InputRequired()], render_kw={"placeholder": "City, State, and Zip"})
    email = EmailField('Email Address', validators=[InputRequired()], render_kw={"placeholder": "Email Here"})
    phoneNum = StringField('Phone Number', validators=[InputRequired()], render_kw={"placeholder": "Phone Number Here"})
    desc = StringField('Description of Sales Items', validators=[InputRequired()], render_kw={"placeholder": "Write a Description of What Your Business Does Here"})
    boothNum = IntegerField('Number of Booths', validators=[InputRequired(), validate_boothNum_loc_match])
    boothLoc = StringField('Booth Location(s)', validators=[InputRequired(), validate_boothLoc_admin], render_kw={"placeholder": "Booth Location(s) here"})
    tableNum = IntegerField('Number of Tables', validators=[InputRequired(), NumberRange(min=0, max=20)])
    date = DateTimeField('Date and Time', format='%H:%M:%S %m-%d-%Y', default=datetime.strptime(datetime.now(pytz.timezone('US/Central')).strftime('%H:%M:%S %m-%d-%Y'), '%H:%M:%S %m-%d-%Y'))
    payment_amount = FloatField('Payment Amount', render_kw={"placeholder": "Payment Amount Here"})
    status = SelectField(u'Status', choices=[('pendingApproval', 'Pending Approval'), ('pendingPayment', 'Pending Payment'), ('denied', 'Denied'), ('finalized', 'Finalized')])
    submit = SubmitField('Save Changes')

class AdminForm(FlaskForm):
    payment_deadline = DateTimeField('Date and Time', format='%Y/%m/%d %H:%M:%S')
    notes = CKEditorField('Note Editor', validators=[InputRequired()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "username"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "password"})
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')