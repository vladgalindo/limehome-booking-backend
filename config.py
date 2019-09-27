import os
from datetime import timedelta


class Config(object):
    # App
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    SECRET_KEY = os.getenv('SECRET_KEY', 'LIME$4laa4l@9%Home')
    APP_PORT = os.getenv('APP_PORT', 5000)
    APP_URL_PREFIX = os.getenv('APP_URL_PREFIX', "/api/v1.0")
    os.environ['APP_URL_PREFIX'] = APP_URL_PREFIX

    # MongoDB cloud service
    DB_HOST = os.getenv('DB_HOST', 'ds217078.mlab.com')
    DB_USER = os.getenv('DB_USER', 'limehomeadmin')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'LIMErlaarl9')
    DB_PORT = os.getenv('DB_PORT', 17078)
    DB_NAME = os.getenv('DB_NAME', 'limehomebooking')
    MONGO_URI = f'''mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?retryWrites=false'''
    MONGODB_HOST = f'''mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?retryWrites=false'''



    # Email service
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_USER', "familiaperezrondon@gmail.com")
    os.environ['MAIL_DEFAULT_SENDER'] = MAIL_DEFAULT_SENDER
    MAIL_USERNAME = os.getenv('MAIL_USER', "familiaperezrondon@gmail.com")
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', "p3r3zr0nd0n")
    MAIL_SERVER = os.getenv('MAIL_SERVER', "smtp.gmail.com")
    MAIL_PORT = os.getenv('MAIL_PORT', "587")
    MAIL_USE_TLS = True
    ACTIVATION_URL = os.getenv('ACTIVATION_URL', 'https://limehome-backend.appspot.com{url_prefix}/users/activate/{id}')
    os.environ['ACTIVATION_URL'] = ACTIVATION_URL
    # JWT
    JWT_SECRET_KEY = SECRET_KEY
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=3)
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

    # Redis cloud service
    REDIS_HOST = os.getenv('REDIS_HOST', 'redis-15255.c55.eu-central-1-1.ec2.cloud.redislabs.com')
    REDIS_PORT = os.getenv('REDIS_HOST', 15255)
    REDIS_DB = os.getenv('REDIS_DB', 0)
    REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', 'T6pvOSFTHT8l2dHqEIYhG35MjP5kB9yk')
    ERROR_INCLUDE_MESSAGE = False

    # BFF
    HERE_PLACES_URL = os.getenv('HERE_PLACES_URL', 'https://places.cit.api.here.com/places/v1/discover/explore')
    os.environ['HERE_PLACES_URL'] = HERE_PLACES_URL
    HERE_APP_ID = os.getenv('HERE_APP_ID', 'iw8thRxwHyaYmlzB4nL3')
    os.environ['HERE_APP_ID'] = HERE_APP_ID
    HERE_APP_CODE = os.getenv('HERE_APP_CODE', 'Jj1JJy-8n3nUWjXoZVA_Kg')
    os.environ['HERE_APP_CODE'] = HERE_APP_CODE

class Development(Config):
    DEBUG = True


class Production(Config):
    DEBUG = False

class Testing(Config):
    DEBUG = True
    TESTING = True
    # MongoDB cloud service
    DB_HOST = os.getenv('DB_HOST', 'ds047037.mlab.com')
    DB_USER = os.getenv('DB_USER', 'limehometest')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'TESTrlaarl9')
    DB_PORT = os.getenv('DB_PORT', 47037)
    DB_NAME = os.getenv('DB_NAME', 'limetest')
    MONGODB_HOST = f'''mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?retryWrites=false'''
