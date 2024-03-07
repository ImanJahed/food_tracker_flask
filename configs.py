import os


class Config:
    """Base Configurations"""
    CSRF_ENABLE = True
    CSRF_SESSION_KEY = os.urandom(24)
    SECRET_KEY = os.urandom(24)
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))





class ConfigProd(Config):
    """Production Configurations"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ...



class ConfigDev(Config):
    """Development Configurations"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(Config.BASE_DIR, 'app.db')