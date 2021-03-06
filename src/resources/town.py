"""
Define the REST verbs relative to the town
"""

from flask.json import jsonify
from flask.ext.restful import Resource
from flask.ext.restful.reqparse import Argument

from repositories import TownRepository
from util import parse_params


class TownResource(Resource):
    """ Verbs relative to the towns """
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
        return jsonify({'town': town.to_dict()})

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

class UniqueTownResource(Resource):
    """ Verbs relative to a town """
    town_repository = TownRepository()

    def get(self, id):
        """ Get all towns """
        town = self.town_repository.get_by_id(id)
        return jsonify({'town': town.to_dict()})
