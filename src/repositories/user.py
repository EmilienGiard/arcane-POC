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

    def update(self, birth_date, id, name, password):
        """ Update the user matching the given id """
        user = self.get_by_id(id)
        user.birth_date = birth_date
        user.name = name
        user.password = password
        return user.save()

    @staticmethod
    def get_by_id(id):
        """ Retrieve a user matching the given id """
        user = User.query.filter_by(id=id).first()
        return user
