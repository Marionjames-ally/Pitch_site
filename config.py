
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/pitch'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = True



    #email configuration
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

   

class ProdConfig(Config):
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:12345@localhost/pitch'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
