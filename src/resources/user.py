"""
Define the REST verbs relative to the user
"""

from flask.ext.restful import Resource
from flask.json import jsonify


class UserResource(Resource):
    """ Verbs relative to the list of users """

    @staticmethod
    def get():
        """ Get all users """
        return 'Test env', 200
