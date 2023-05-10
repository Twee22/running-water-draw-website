from flask import Flask, url_for
from app import app
from config import Config
from flask_mail import Mail, Message


# configure mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] =  Config.email
app.config['MAIL_PASSWORD'] =  Config.email_password

# create mail instance
mail = Mail(app)

# route to send email
def send_email(user):
    invoice_payment = user.payment_amount
    paypal_link = url_for('payment', id=user.id, _external=True)

    # create message object
    msg = Message('Vendor Application Approved', sender='testemailschool@gmail.com', recipients=[user.email])

    msg.body = f"Dear {user.name},\n\nWe're excited to inform you that your vendor application has been approved! Your invoice amount is ${str(invoice_payment)} and we've generated a PayPal invoice for you to make the payment process quick and easy. To access your invoice, simply click on this link: {paypal_link}. If you have any questions or concerns about the payment process, don't hesitate to reach out to us for assistance.\n\nThank you for joining us and we look forward to working with you!\n\nBest regards"
    # send email
    mail.send(msg)

def application_recieved(user):
    msg = Message('Vendor Application Recieved', sender='testemailschool@gmail.com', recipients=[user.email])

    msg.body = f"Dear {user.name},\n\nYour application has been received.\n\nThank you for applying!"
    # send email
    mail.send(msg)


# route to send email 
def send_payment_confirmation_email(user):
    # create message object
    msg = Message('Payment Received', sender='testemailschool@gmail.com', recipients=[user.email])

    msg.body = f"Dear {user.name},\n\nWe're delighted to inform you that we've received your invoice payment and your booth selection has been confirmed. Thank you for completing the payment process on time.\n\nIf you have any questions or concerns, feel free to contact us for assistance.\n\nBest regards"
    # send confirmation of payment email
    mail.send(msg)


def send_decline_email(user):
    # create message object
    msg = Message('Vendor Application Declined', sender='testemailschool@gmail.com', recipients=[user.email])

    msg.body = f"Dear {user.name},\n\nWe're sorry to inform you that your vendor booth application has been declined. If you have any questions or would like more information, please don't hesitate to reach out to us.\n\nThank you for your interest in our event.\n\nBest regards,\n[Your Name]"
    # send declination of payment email
    mail.send(msg)




