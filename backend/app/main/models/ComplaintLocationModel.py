from . import db


class ComplaintLocationModel(db.Model):
    __tablename__="complaintLocation"
    id = db.Column(db.Integer,primary_key = True)
    complaintID = db.Column(db.Integer, db.ForeignKey("complaint.id"))
    lng = db.Column(db.String(60))
    lat = db.Column(db.String(60))