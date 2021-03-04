from . import db


class ComplaintModel(db.Model):
    __tablename__="complaint"
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey("user.id"))
    subject = db.Column(db.String(60))
    complaint = db.Column(db.String(500))
    status = db.Column(db.Boolean)
    registeredAdmin = db.Column(db.Integer, db.ForeignKey("admin.id"))
