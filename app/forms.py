from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, IntegerField, BooleanField, PasswordField, DateTimeField, FloatField, SelectField
from wtforms.validators import InputRequired, Length, NumberRange, DataRequired, ValidationError
from flask_ckeditor import CKEditorField
from datetime import datetime, timezone
from app.map_contraints import validate_boothLoc, validate_boothLoc_admin, validate_boothNum_loc_match, validate_boothLoc_available,  validate_no_digits, validate_digits, validate_phoneNum, validate_no_special_chars
import pytz

class ApplicationForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), validate_no_digits, validate_no_special_chars], render_kw={"placeholder": "Your Full Name Here"})
    # StringField for name input, with validators for required input, no digits, and no special characters. Placeholder text provided.
    business = StringField('Business Name', validators=[InputRequired()], render_kw={"placeholder": "Business Name Here"})
    # StringField for business name input, with validator for required input. Placeholder text provided.
    address = StringField('Address', validators=[InputRequired()], render_kw={"placeholder": "Address Here"})
    # StringField for address input, with validator for required input. Placeholder text provided.
    citystatezip = StringField('City, State, Zip', validators=[InputRequired()], render_kw={"placeholder": "City, State, and Zip"})
    # StringField for city, state, zip input, with validator for required input. Placeholder text provided.
    email = EmailField('Email Address', validators=[InputRequired()], render_kw={"placeholder": "Email Here"})
    # EmailField for email input, with validator for required input. Placeholder text provided.
    phoneNum = StringField('Phone Number', validators=[InputRequired(), validate_phoneNum], render_kw={"placeholder": "Phone Number Here"})
    # StringField for phone number input, with validators for required input and phone number format. Placeholder text provided.
    desc = StringField('Description of Sales Items', validators=[InputRequired()], render_kw={"placeholder": "Write a Description of What Your Business Does Here"})
    # StringField for description of sales items input, with validator for required input. Placeholder text provided.
    boothNum = IntegerField('Number of Booths', validators=[InputRequired(), validate_boothNum_loc_match, NumberRange(min=1,max=2)], render_kw={"placeholder": "Number of Booths here (max two)"})
    # IntegerField for number of booths input, with validators for required input, booth number and location matching, and range of 1-2 booths. Placeholder text provided.
    boothLoc = StringField('Booth Location(s)', validators=[InputRequired(), validate_boothLoc, validate_boothLoc_available], render_kw={"placeholder": "Booth Location(s) Here"})
    # StringField for booth location input, with validators for required input, valid booth location, and availability of chosen booth location. Placeholder text provided.
    tableNum = IntegerField('Number of Tables', validators=[InputRequired(), NumberRange(min=0, max=20)] , render_kw={"placeholder": "Number of Tables Here"})
    # IntegerField for number of tables input, with validators for required input and range of 0-20 tables. Placeholder text provided.
    date = DateTimeField('Date and Time', format='%H:%M:%S %m-%d-%Y', default=datetime.strptime(datetime.now(pytz.timezone('US/Central')).strftime('%H:%M:%S %m-%d-%Y'), '%H:%M:%S %m-%d-%Y'))
    # DateTimeField for date and time input, with format set to hour:minute:second month-day-year in US/Central timezone. Default value is the current date and time.
    terms = BooleanField('I have read and agree to this:', validators=[InputRequired()])
    # BooleanField for agreement to terms and conditions, with validator for required input.
    # sign = StringField('Signed', validators=[InputRequired()])
    # This line is commented out, indicating that it is not currently being used.
    submit = SubmitField('Submit')
    # SubmitField for submitting the form. Labelled as "Submit".


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
    payment_amount = FloatField('Payment Amount', validators=[InputRequired(), validate_digits], render_kw={"placeholder": "Payment Amount Here"})
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
    payment_amount = FloatField('Payment Amount', validators=[InputRequired(), validate_digits], render_kw={"placeholder": "Payment Amount Here"})
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