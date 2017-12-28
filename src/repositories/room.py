""" Define the Room repository """

from models import Room


class RoomRepository:
    """ The repository for the Room model """

    @staticmethod
    def create(characteristic, property_id):
        """ Create a room """
        room = Room(characteristic=characteristic, property_id=property_id).save()
        return room

    def update(self, id, characteristic):
        """ Update the room matching the given id """
        room = self.get_by_id(id)
        room.characteristic = characteristic
        return room.save()

    @staticmethod
    def get_by_id(id):
        """ Retrieve a room matching the given id """
        room = Room.query.filter_by(id=id).first()
        return room
