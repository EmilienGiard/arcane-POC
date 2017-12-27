"""
Defines the blueprint for the town
"""
from flask import Blueprint
from flask.ext.restful import Api

from resources import TownResource


TOWN_BLUEPRINT = Blueprint('town', __name__)
Api(TOWN_BLUEPRINT).add_resource(TownResource, '/town')
