""" Define the Property repository """

from models import Property
from repositories import RoomRepository


class PropertyRepository:
    """ The repository for the Property model """
    room_repository = RoomRepository()

    def create(self, description, name, owner_id, rooms, town_id, type):
        """ Create a property """
        property = Property(
            description=description,
            name=name,
            owner_id=owner_id,
            town_id=town_id,
            type=type
            ).save()
        property = self.create_property_rooms(property, rooms)
        return property

    @staticmethod
    def get():
        """ Query all properties """
        properties = Property.query.all()
        return properties

    @staticmethod
    def get_by_id(id):
        """ Retrieve a property matching the given id """
        property = Property.query.filter_by(id=id).first()
        return property

    def create_property_rooms(self, property, rooms):
        """ Create translations for a given property """

        for room in rooms:
            room = self.room_repository.create(
                characteristic=room['characteristic'],
                property_id=property.id,
            )

        return property

    def update(self, id, description, name, owner_id, rooms, town_id, type):
        """ Update the property matching the given id """
        property = self.get_by_id(id)
        if property.owner_id == owner_id:
            property.description = description
            property.name = name
            property.owner_id = owner_id
            property.town_id = town_id
            property.type = type
            property = self.update_property_rooms(property, rooms)
        return property.save()

    def update_property_rooms(self, property, rooms):
        """ Create translations for a given property """

        for room in rooms:
            room = self.room_repository.update(
                id=room['id'],
                characteristic=room['characteristic'],
            )

        return property
