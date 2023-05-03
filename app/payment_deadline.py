from app import db
import datetime

def set_deadline():
    days = 14
    return days

def save_initial_time():
    initial = datetime.datetime.now()
    return initial

def future_times():
    current_time = datetime.datetime.now()
    future_time = current_time + datetime.timedelta(days=set_deadline())
    return future_time

def check_time(deadline):
    current_time = datetime.datetime.now()
    elapsed_time = current_time - deadline
    return elapsed_time.days >= set_deadline()
    
def check_db(vendors):
    for vendor in vendors:
        if check_time(vendor.payment_deadline):
            vendor.status = 'deadlineReached'

    db.session.commit()


