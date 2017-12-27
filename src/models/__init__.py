from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .town import Town
from .user import User
