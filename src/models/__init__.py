from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .property import Property
from .town import Town
from .user import User
