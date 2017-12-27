""" Define the Town repository """

from models import Town


class TownRepository:
    """ The repository for the Town model """

    @staticmethod
    def create(name):
        """ Create a town """
        town = Town(name=name).save()
        return town

    @staticmethod
    def get():
        """ Query all towns """
        towns = Town.query.all()
        return towns

    def update(self, id, name):
        """ Update the town matching the given id """
        town = self.get_by_id(id)
        town.name = name
        return town.save()

    @staticmethod
    def get_by_id(id):
        """ Retrieve a town matching the given id """
        town = Town.query.filter_by(id=id).first()
        return town
