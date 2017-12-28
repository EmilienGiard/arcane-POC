"""
Define the town model
"""

from . import db
from .abc import BaseModel


class Town(db.Model, BaseModel):
    """ The town model """
    __tablename__ = 'town'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    properties = db.relationship('Property', backref='property')

    def __init__(self, name):
        """ Create a new town """
        self.name = name

    def to_dict(self):
        """ Return a dict representation of the town model """
        return {
            'id': self.id,
            'name': self.name,
        }
