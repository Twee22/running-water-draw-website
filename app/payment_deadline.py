from app import db
import datetime

payment_deadline_days = 14

def set_deadline(new_deadline):
    global payment_deadline_days
    payment_deadline_days = new_deadline

def get_deadline():
    return payment_deadline_days

def save_initial_time():
    initial = datetime.datetime.now()
    return initial

def future_times():
    current_time = datetime.datetime.now()
    future_time = current_time + datetime.timedelta(days=get_deadline())
    return future_time

def check_time(deadline):
    current_time = datetime.datetime.now()
    elapsed_time = current_time - deadline
    return elapsed_time.days >= get_deadline()

def check_db(vendors):
    for vendor in vendors:
        if check_time(vendor.payment_deadline):
            vendor.status = 'deadlineReached'

    db.session.commit()
