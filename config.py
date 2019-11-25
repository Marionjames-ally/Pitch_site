import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = "marion"
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    

    DEBUG = True

class TestConfig(Config):
    '''
    child test configuration class
    '''
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}