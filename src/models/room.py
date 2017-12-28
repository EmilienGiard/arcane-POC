"""
Define the room model
"""

from . import db
from .abc import BaseModel


class Room(db.Model, BaseModel):
    """ The room model """
    __tablecharacteristic__ = 'room'

    id = db.Column(db.Integer, primary_key=True)
    characteristic = db.Column(db.String(200), nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=False)

    def __init__(self, characteristic, property_id):
        """ Create a new room """
        self.characteristic = characteristic
        self.property_id = property_id

    def to_dict(self):
        """ Return a dict representation of the room model """
        return {
            'id': self.id,
            'characteristic': self.characteristic,
            'property_id': self.property_id,
        }
