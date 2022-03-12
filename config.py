import os 

class Config:
    SECRET_KEY = b'&/\xf8>\x13[\xcd8\xf1S4\x8b\xf0\xa0F\xb3c\x96\x9c\x05\xcb\xc6/#\x0c\xb1)\xe1\xde\x89\x9d\xce'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:moringa@localhost/myblog'
    UPLOADED_PHOTOS_DEST = "app/static/photos"

    # email configurations
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','')
    if SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres://', "postgresql://", 1)

class TestConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:vyonna6519@localhost/blog_test"

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:vyonna6519@localhost/myblog"
    DEBUG = True


config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig
}