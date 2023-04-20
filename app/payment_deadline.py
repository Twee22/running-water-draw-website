from app import db
import datetime

def save_initial_time():
    initial = datetime.datetime.now()
    return initial

def check_time(initial):
    current_time = datetime.datetime.now()
    elapsed_time = current_time - initial
    if elapsed_time.days >= 14:
        return True
    else:
        return False
def check_db(vendors):
    for vendor in vendors:
        if check_time(vendor.payment_deadline):
            x = x
            #vendor.status = 'deadLineReached'

    db.session.commit()

