from flask import Flask
from app import app
from flask_mail import Mail, Message


# configure mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'testemailschool50@gmail.com' # enter your email address here
app.config['MAIL_PASSWORD'] = 'zktfwkjnfxnnttfk' # enter your email password here

# create mail instance
mail = Mail(app)

# route to send email
def send_email(user_email):
    invoice_payment = "getPaymentAmount"
    paypal_link = "https://www.paypal.com/us/webapps/mpp/account-selection?kid=p75883314412&gclid=CjwKCAjw6IiiBhAOEiwALNqncWyRm_HXRwkEhvR-bfC4g4bFgvYR-rJyxKobopBzKR32wrGTyljbExoChtAQAvD_BwE&gclsrc=aw.ds"

    # create message object
    msg = Message('Vendor Application Approved', sender='testemailschool@gmail.com', recipients=[user_email])
    msg.body = 'Your vendor application has been approved, your invoice amount is' + invoice_payment + 'Here is a link to your invoice #: ' + paypal_link

    # send email
    mail.send(msg)
