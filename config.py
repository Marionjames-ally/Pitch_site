import os

class Config:
    debug = True
    SECRET_KEY = 'marion'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = True


    ##email config
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USER_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    ## simplemde configs
    SIMPLEMDE_JS = True
    SIMPLEMDE_USE_CDN = True

class prodConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:1234@localhost/pitch'
    DEBUG=True

config_options={
    'development':DevConfig,
    'production':prodConfig
}
