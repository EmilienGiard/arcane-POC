""" Define the User repository """

from models import User


class UserRepository:
    """ The repository for the User model """

    @staticmethod
    def create(birth_date, name, password):
        """ Create a user """
        user = User(birth_date=birth_date, name=name, password=password).save()
        return user

    @staticmethod
    def get():
        """ Query all users """
        users = User.query.all()
        return users
