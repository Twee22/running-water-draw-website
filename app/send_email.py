from flask import Flask, url_for
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
def send_email(user):
    invoice_payment = user.payment_amount
    paypal_link = url_for('payment', id = user.id, _external=True)

    # create message object
    msg = Message('Vendor Application Approved', sender='testemailschool@gmail.com', recipients=[user.email])
    msg.body = f'Your vendor application has been approved, your invoice amount is ${str(invoice_payment)}. Here is a link to your invoice: {paypal_link}'

    # send email
    mail.send(msg)



