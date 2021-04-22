import os
basedir = os.path.abspath(os.path.dirname(__file__))





class Config(object):

    database_path = os.environ['DATABASE_URL']
    if database_path.startswith("postgres://"):
        database_path = database_path.replace("postgres://", "postgresql://", 1)

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    SQLALCHEMY_BINDS = {
    'dev_db': database_path,
    'test_db': 'postgresql://localhost/wineport_test_db'
}


class ProductionConfig(Config):
    
    DEVELOPMENT = False
    DEBUG = False

    database_path = os.environ['DATABASE_URL']
    if database_path.startswith("postgres://"):
        database_path = database_path.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = database_path


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    database_path = os.environ['DATABASE_URL']
    if database_path.startswith("postgres://"):
        database_path = database_path.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = database_path



class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/wineport_test_db'
    DEBUG = False




