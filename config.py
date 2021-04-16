import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
database_path = os.environ['DATABASE_URL']

if database_path.startswith("postgres://"):
    database_path = database_path.replace("postgres://", "postgresql://", 1)

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = database_path

SQLALCHEMY_TRACK_MODIFICATIONS = False
