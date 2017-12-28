"""
Define the property model
"""
from . import db
from .abc import BaseModel


class Property(db.Model, BaseModel):
    """ The property model """
    __tablename__ = 'property'

    description = db.Column(db.String(500), nullable=False)
    type = db.Column(db.String(50), nullable=True)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    town_id = db.Column(db.Integer, db.ForeignKey('town.id'), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, description, name, owner_id, town_id, type):
        """ Create a new property """
        self.description = description
        self.name = name
        self.owner_id = owner_id
        self.town_id = town_id
        self.type = type

    def to_dict(self):
        """ Return a dict representation of the property model """
        return {
            'description': self.description,
            'id': self.id,
            'name': self.name,
            'owner_id': self.owner_id,
            'town_id': self.town_id,
            'type': self.type,
        }
