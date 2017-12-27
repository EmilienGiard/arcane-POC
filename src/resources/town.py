"""
Define the REST verbs relative to the town
"""

from flask.json import jsonify
from flask import request
from flask.ext.restful import Resource, inputs
from flask.ext.restful.reqparse import Argument

from repositories import TownRepository
from util import parse_params


class TownResource(Resource):
    """ Verbs relative to the list of towns """
    town_repository = TownRepository()

    def get(self):
        """ Get all towns """
        towns = self.town_repository.get()
        return jsonify({'towns': [town.to_dict() for town in towns]})

    @parse_params(
        Argument('name', location='json', type=str, required=True),
    )
    def post(self, name):
        """ Create a town """
        town = self.town_repository.create(name)
        return town.to_dict()

    @parse_params(
        Argument('id', location='json', type=int, required=True),
        Argument('name', location='json', type=str, required=True),
    )
    def put(self, id, name):
        """ Update a town """
        town = TownRepository().update(
            id=id,
            name=name,
        )
        return jsonify({'town': town.to_dict()})
