"""
Define the REST verbs relative to the user
"""

from flask.json import jsonify
from flask import request
from flask.ext.restful import Resource, inputs
from flask.ext.restful.reqparse import Argument

from repositories import UserRepository
from util import parse_params


class UserResource(Resource):
    """ Verbs relative to the users """
    user_repository = UserRepository()

    def get(self):
        """ Get all users """
        users = self.user_repository.get()
        return jsonify({'users': [user.to_dict() for user in users]})

    @parse_params(
        Argument('birth_date', location='json', type=inputs.date, required=True),
        Argument('name', location='json', type=str, required=True),
        Argument('password', location='json', type=str, required=True),
    )
    def post(self, birth_date, name, password):
        """ Create a user """
        user = self.user_repository.create(birth_date, name, password)
        return user.to_dict()

    @parse_params(
        Argument('birth_date', location='json', type=inputs.date, required=True),
        Argument('id', location='json', type=int, required=True),
        Argument('name', location='json', type=str, required=True),
        Argument('password', location='json', type=str, required=True),
    )
    def put(self, birth_date, id, name, password):
        """ Update a user """
        user = UserRepository().update(
            birth_date=birth_date,
            id=id,
            name=name,
            password=password,
        )
        return jsonify({'user': user.to_dict()})
