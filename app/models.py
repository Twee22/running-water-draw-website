from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(50), nullable=False)
    business = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    citystatezip = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phoneNum = db.Column(db.String(20), nullable=False)
    desc = db.Column(db.Text)
    boothNum = db.Column(db.Integer, nullable=False)
    tableNum = db.Column(db.Integer)

    def __repr__(self):
        return '<Vendor {}>'.format(self.business)
    