import os
import logging

DEBUG = True
APPLICATION_ROOT = '/arcane-poc'
HOST = '0.0.0.0'
PORT = 5000

DB_CONTAINER = 'DB'

DATABASE = {
    'user': 'postgres',
    'pw': '',
    'host': DB_CONTAINER,
    'port': 5432,
    'db': 'postgres',
}

DB_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % DATABASE

logging.basicConfig(
    filename=os.getenv('SERVICE_LOG', 'server.log'),
    level=logging.DEBUG,
    format='%(levelname)s: %(asctime)s pid:%(process)s module:%(module)s %(message)s',
    datefmt='%d/%m/%y %H:%M:%S',
)
