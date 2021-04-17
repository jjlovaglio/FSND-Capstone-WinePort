import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {
    'dev_db': 'postgresql://localhost/wineport_dev_db',
    'test_db':'postgresql://localhost/wineport_test_db'
}


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/wineport_dev_db"



class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/wineport_test_db"




# if database_path.startswith("postgres://"):
#     database_path = database_path.replace("postgres://", "postgresql://", 1)

# # TODO IMPLEMENT DATABASE URL
# SQLALCHEMY_DATABASE_URI = database_path

