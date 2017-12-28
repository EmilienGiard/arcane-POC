"""
Define the user model
"""
from . import db
from .abc import BaseModel


class User(db.Model, BaseModel):
    """ The user model """
    __tablename__ = 'user'

    birth_date = db.Column(db.DateTime, nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    properties = db.relationship('Property', backref='property')

    def __init__(self, birth_date, name, password):
        """ Create a new user """
        self.birth_date = birth_date
        self.name = name
        self.password = password

    def to_dict(self):
        """ Return a dict representation of the user model """
        return {
            'birth_date': self.birth_date.strftime('%m-%d-%Y'),
            'id': self.id,
            'name': self.name,
            'password': self.password,
        }
