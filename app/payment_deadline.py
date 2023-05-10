from app import db
from flask import session
import datetime

# Set a default payment deadline of 14 days
payment_deadline_days = 14

# Allow admin to set a new payment deadline
def set_deadline(new_deadline):
    global payment_deadline_days
    payment_deadline_days = new_deadline

# Get the current payment deadline
def get_deadline():
    return payment_deadline_days

# Check if submission is before the deadline
import datetime

def is_before_deadline(submission_date, deadline_date):
    # Convert submission_date to date object to compare with deadline_date
    if deadline_date is None:
        # handle the case where deadline_date is not set
        return True
    submission_date = submission_date.date()
    deadline_date = datetime.datetime.strptime(deadline_date.strftime('%Y-%m-%d'), '%Y-%m-%d').date() # Convert date to string and then to datetime object
    return submission_date < deadline_date



# Get the initial time of payment submission
def save_initial_time():
    initial = datetime.datetime.now()
    return initial

# Calculate booth price based on submission date and deadline date
def get_booth_price(form_data, deadline_date):
    one_booth_price = session.get('one_booth_price', 0)
    two_booths_price = session.get('two_booths_price', 0)
    one_booth_post_cutoff_price = session.get('one_booth_post_cutoff_price', 0)
    two_booths_post_cutoff_price = session.get('two_booths_post_cutoff_price', 0)

    if form_data.boothNum.data == 1:
        if is_before_deadline(form_data.date.data, deadline_date):
            boothPrice = one_booth_price
        else:
            boothPrice = one_booth_post_cutoff_price
    else:
        if is_before_deadline(form_data.date.data, deadline_date):
            boothPrice = two_booths_price
        else:
            boothPrice = two_booths_post_cutoff_price

    return boothPrice


# This function calculates the future date and time based on the current time and the deadline set
def future_times():
    current_time = datetime.datetime.now()
    # timedelta is used to add or subtract days, weeks, hours, minutes, seconds, etc. from a date
    future_time = current_time + datetime.timedelta(days=get_deadline())
    return future_time

# This function checks if the elapsed time between the current time and the deadline has exceeded the payment deadline
def check_time(deadline):
    current_time = datetime.datetime.now()
    # Subtracting the deadline from the current time will give us the elapsed time
    elapsed_time = current_time - deadline
    # If the elapsed time in days is greater than or equal to the payment deadline, return True
    return elapsed_time.days >= get_deadline()

# This function checks the payment deadlines for all vendors in the database and sets the status to 'deadlineReached' if necessary
def check_db(vendors):
    for vendor in vendors:
        if vendor.status == 'pendingPayment' and check_time(vendor.payment_deadline):
            vendor.status = 'deadlineReached'
    # Commit the changes to the database
    db.session.commit()

