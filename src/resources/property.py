"""
Define the REST verbs relative to the property
"""

from flask.json import jsonify
from flask import request
from flask.ext.restful import Resource, inputs
from flask.ext.restful.reqparse import Argument

from repositories import PropertyRepository
from util import parse_params


class PropertyResource(Resource):
    """ Verbs relative to the properties """
    property_repository = PropertyRepository()

    @parse_params(
        Argument('description', location='json', type=str, required=True),
        Argument('name', location='json', type=str, required=True),
        Argument('owner_id', location='json', type=int, required=True),
        Argument('rooms', location='json', type=list, required=True),
        Argument('town_id', location='json', type=int, required=True),
        Argument('type', location='json', type=str, required=True),
    )
    def post(self, description, name, owner_id, rooms, town_id, type):
        """ Create a property """
        property = self.property_repository.create(
            description=description,
            name=name,
            owner_id=owner_id,
            rooms=rooms,
            town_id=town_id,
            type=type)
        return property.to_dict()

    @parse_params(
        Argument('description', location='json', type=str, required=True),
        Argument('id', location='json', type=int, required=True),
        Argument('name', location='json', type=str, required=True),
        Argument('owner_id', location='json', type=int, required=True),
        Argument('rooms', location='json', type=list, required=True),
        Argument('town_id', location='json', type=int, required=True),
        Argument('type', location='json', type=str, required=True),
    )
    def put(self, description, id, name, owner_id, rooms, town_id, type):
        """ Create a property """
        property = self.property_repository.update(
            description=description,
            id=id,
            name=name,
            owner_id=owner_id,
            rooms=rooms,
            town_id=town_id,
            type=type)
        return property.to_dict()
