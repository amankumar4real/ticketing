from . import db


class AdminModel(db.Model):
    __tablename__="admin"
    id = db.Column(db.Integer,primary_key = True)
    firstname = db.Column(db.String(60))
    lastname = db.Column(db.String(60))
    email = db.Column(db.String(60),unique = True)
    password = db.Column(db.String(60))
    profilePicture = db.Column(db.String(300))
    dataOfRegister = db.Column(db.Date)
    designation = db.Column(db.String(60))
    lng = db.Column(db.String(60))
    lat = db.Column(db.String(60))
