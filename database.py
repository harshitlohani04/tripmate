from app import db
import json

class User(db.Model):
    __tablename__ = "trip_data"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    number_of_members = db.Column(db.Integer)
    days = db.Column(db.Integer)
    travel_with = db.Column(db.String(100))
    type_of_group = db.Column(db.String(50))
    destination = db.Column(db.String(100))
    plan = db.Column(db.Text)

    def __repr__(self): # for debugging
        return f"{self.plan}"
