import os 

class Config:
    SECRET_KEY =  '562af35a9b244efba09ef9e1a482d134x9'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:vyonna6519@localhost/myblog'
    UPLOADED_PHOTOS_DEST = "app/static/photos"

    SQLALCHEMY_TRACK_MODIFICATIONS=False


    # email configurations
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'vyonna.njenga@student.moringaschool.com'
    MAIL_PASSWORD = 'vyonnamoringa6519'

class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
       SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    pass 

class TestConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:vyonna6519@localhost/myblog"

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:vyonna6519@localhost/myblog"
    DEBUG = True


config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig
}