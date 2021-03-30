from flask_sqlalchemy import SQLAlchemy
from application import db

class Stage1(db.Model):
    """Primer stage de informacion
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    datetime = db.Column(db.DateTime)

class Contact(db.Model):
    """donde cae la info de contact
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(255))
    company = db.Column(db.String(100))
    service = db.Column(db.String(100))
    tellusmore = db.Column(db.String(255))
    datetime = db.Column(db.DateTime)

db.create_all()