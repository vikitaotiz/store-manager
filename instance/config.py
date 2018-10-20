import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """ Configuration class """
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    """ Configuration for development """
    DEBUG = True
    TESTING = False

class TestingConfig(Config):
    """ Configuration for testing """
    DEBUG = True
    TESTING = False

class StagingConfig(Config):
    """ Configuration class """
    DEBUG = True

class ProductionConfig(Config):
    """ Configuration for production """
    DEBUG = True
    TESTING = False

app_config = {
    "development" : DevelopmentConfig,
    "testing" : TestingConfig,
    "staging" : StagingConfig,
    "production" : ProductionConfig
}