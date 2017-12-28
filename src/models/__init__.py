from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .property import Property
from .room import Room
from .town import Town
from .user import User
