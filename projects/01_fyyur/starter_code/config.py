import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
username = 'postgres'
password = '1234'
db_name = 'fyuur'
# postgresql://[username]:[password]@localhost:5432/[db_name]
SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}/{}".format(
    username,
    password,
    'localhost:5432',
    db_name
)

SQLALCHEMY_TRACK_MODIFICATIONS = True
