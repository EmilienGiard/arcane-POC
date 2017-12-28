"""
Defines the blueprint for the property
"""
from flask import Blueprint
from flask.ext.restful import Api

from resources import PropertyResource


PROPERTY_BLUEPRINT = Blueprint('property', __name__)
Api(PROPERTY_BLUEPRINT).add_resource(PropertyResource, '/property')
