import os
basedir = os.path.abspath(os.path.dirname(__file__))

database_path = os.environ['DATABASE_URL']

if database_path.startswith("postgres://"):
    database_path = database_path.replace("postgres://", "postgresql://", 1)


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {
    'dev_db': os.environ['DATABASE_URL'],
    'test_db':os.environ['TEST_DATABASE_URL']
}


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = database_path


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']



class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ['TEST_DATABASE_URL']
    DEBUG = False




