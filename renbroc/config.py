import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
    Base configuration, extended by classes below.
    """
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'renbroc.db')
    #SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

    WTF_CSRF_ENABLED = True
    VERSION = '0.1.0'
    DEBUG = True
    SECURITY_TRACKABLE = True
    SECRET_KEY = 'This is not a good secret key.'

class LocalConfig(Config):
    """
    Config used when running locally
    """
    DEBUG = True
    #TESTING = True

class DevelopmentConfig(Config):
    """
    Config used on the development server.
    """
    DEBUG = True
    #TESTING = False

class TestingConfig(Config):
    """
    Config used when running tests
    """
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    """
    Config used in production.
    """
    DEBUG = False
    #TESTING = False
