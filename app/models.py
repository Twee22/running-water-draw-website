from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import func
import datetime

user_vendor = db.Table('user_vendor',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('vendor_id', db.Integer, db.ForeignKey('vendor.id'))
)

class User(db.Model):  # Define a model for the User table in the database.
    id = db.Column(db.Integer, primary_key=True)  # Define an id column as the primary key.
    username = db.Column(db.String(64), index=True, unique=True)  # Define a username column with an index and unique constraint.
    email = db.Column(db.String(120), index=True)  # Define an email column with an index.
    password_hash = db.Column(db.String(128))  # Define a password_hash column to store hashed passwords.
    following = db.relationship('Vendor', secondary=user_vendor, backref='followers')  # Define a many-to-many relationship between the User and Vendor tables.

    def __repr__(self):
        return '<User {}>'.format(self.username)  # Define a string representation for the User object.

    def set_password(self, password):  # Define a method to set the password for a User object.
        self.password_hash = generate_password_hash(password)  # Hash the password and store it in the password_hash column.

    def check_password(self, password):  # Define a method to check if a given password matches the User object's password.
        return check_password_hash(self.password_hash, password)  # Return True if the password matches, False otherwise.

    
# Defining a class named Vendor which inherits from db.Model
class Vendor(db.Model):
    # Defining columns for the table Vendor using db.Column() method
    id = db.Column(db.Integer, primary_key=True)           # Primary key column for the table
    name = db.Column(db.String(50), nullable=False)        # Name of the vendor, cannot be null
    business = db.Column(db.String(200), nullable=False)   # Name of the business, cannot be null
    address = db.Column(db.String(200), nullable=False)    # Address of the vendor, cannot be null
    citystatezip = db.Column(db.String(50), nullable=False)# City, state, and ZIP of the vendor, cannot be null
    email = db.Column(db.String(120), nullable=False)      # Email of the vendor, cannot be null
    phoneNum = db.Column(db.String(20), nullable=False)    # Phone number of the vendor, cannot be null
    desc = db.Column(db.Text)                              # Description of the vendor
    boothNum = db.Column(db.Integer, nullable=False)       # Booth number of the vendor, cannot be null
    boothLoc = db.Column(db.String, nullable=False)        # Booth location of the vendor, cannot be null
    tableNum = db.Column(db.Integer)                       # Table number of the vendor
    date = db.Column(db.DateTime(timezone=True), server_default=func.now()) # Date column with default value as current date and time
    payment_deadline = db.Column(db.DateTime(timezone=True), server_default=func.now()) # Payment deadline column with default value as current date and time
    payment_amount = db.Column(db.Float, nullable=False)   # Payment amount of the vendor, cannot be null
    status = db.Column(db.String, nullable=False)          # Status of the vendor, cannot be null
    year = db.Column(db.Integer, nullable=False)           # Year of the vendor, cannot be null
    one_booth_price = db.Column(db.Float, nullable=False, server_default='150')
    twp_booths_price = db.Column(db.Float, nullable=False, server_default='200')
    one_booth_post_cutoff_price = db.Column(db.Float, nullable=False, server_default='175')
    two_booths_post_cutoff_price = db.Column(db.Float, nullable=False, server_default='225')
    deadline_date = db.Column(db.DateTime(timezone=True), server_default=datetime.datetime(2023, 7, 1).isoformat())

    def __repr__(self):
        return '<Vendor {}>'.format(self.business)
    
    def __iter__(self):
        return iter([str(self.id), str(self.name), str(self.business), str(self.address), 
                        str(self.citystatezip), str(self.email), str(self.phoneNum), str(self.desc), str(self.boothNum), 
                        str(self.boothLoc), str(self.tableNum), str(self.date), str(self.payment_amount), str(self.payment_deadline), str(self.status)])
    
class AppText(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String, nullable=False)
    festival_number = db.Column(db.String, nullable=False, server_default='49th')
    
class CurrentYear(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))