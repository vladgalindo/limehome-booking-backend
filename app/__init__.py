import os
from flask import Flask, url_for
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_restplus import Api
from pymongo import MongoClient
from redis import StrictRedis
from flask_cors import CORS
from flask_google_cloud_logger import FlaskGoogleCloudLogger
from app.common.cloud_logger import logger


# App
app = Flask(__name__)
app.config.from_object(os.getenv('FLASK_ENVIRONMENT', 'config.Development'))
FlaskGoogleCloudLogger(app)
CORS(app)
# Email service
email = Mail(app)

# MongoDB
mongo_bd_conn = MongoClient(app.config['MONGO_URI'])
mongo_bd = mongo_bd_conn[app.config['DB_NAME']]

# Redis
redis_db = StrictRedis(
    host=app.config['REDIS_HOST'],
    port=app.config['REDIS_PORT'],
    db=app.config['REDIS_DB'],
    password=app.config['REDIS_PASSWORD'],
    decode_responses=True
)

# JWT
jw_token = JWTManager(app)
@jw_token.token_in_blacklist_loader
def check_invalid_token(token):
    jti = token['jti']
    registry = redis_db.get(jti)
    if registry is None:
        return True
    return registry == 'true'


if os.getenv('FLASK_ENVIRONMENT') == "config.Production":
    @property
    def specs_url(self):
        return url_for(self.endpoint('specs'), _external=True, _scheme='https')

    Api.specs_url = specs_url
api = Api(app, title='LimeHome Booking App', description='LimeHome App', version=1.0)
@api.errorhandler(Exception)
def error_handler(err):
    error_code = err.code
    sms = err.__str__
    return {"error_code": error_code, "sms": sms}, error_code

@app.template_filter()
def date_custom_filter(value, format='%Y/%m/%d'):
    return value.strftime(format)

app.jinja_env.filters['customdate'] = date_custom_filter