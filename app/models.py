from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import func

user_vendor = db.Table('user_vendor',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('vendor_id', db.Integer, db.ForeignKey('vendor.id'))
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    following = db.relationship('Vendor', secondary=user_vendor, backref='followers')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    business = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    citystatezip = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phoneNum = db.Column(db.String(20), nullable=False)
    desc = db.Column(db.Text)
    boothNum = db.Column(db.Integer, nullable=False)
    boothLoc = db.Column(db.String, nullable=False)
    tableNum = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    status = db.Column(db.String, nullable=False)


    def __repr__(self):
        return '<Vendor {}>'.format(self.business)
    
    def __iter__(self):
        return iter([str(self.id), str(self.name), str(self.business), str(self.address), 
                        str(self.citystatezip), str(self.email), str(self.phoneNum), str(self.desc), str(self.boothNum), 
                        str(self.boothLoc), str(self.tableNum), str(self.date), str(self.status)])
    
class AppText(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String, nullable=False)
    
@login.user_loader
def load_user(id):
    return User.query.get(int(id))