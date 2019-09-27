import os
from flask import Flask
from flask_cors import CORS
from flask_mail import Mail
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from redis import StrictRedis

if os.getenv('FLASK_ENV') == 'development' or None:
    config='config.Development'
elif os.getenv('FLASK_ENV') == 'production':
    config = 'config.Production'
else:
    config = 'config.Testing'

db = MongoEngine()
email = Mail()

#def create_app(config_name='config.Development'):
app = Flask(__name__)

app.config.from_object(config)
CORS(app)
try:
    db.init_app(app)
except Exception as e:
    print(e)

email.init_app(app)

# Redis
redis_db = StrictRedis(
    host=app.config['REDIS_HOST'],
    port=app.config['REDIS_PORT'],
    db=app.config['REDIS_DB'],
    password=app.config['REDIS_PASSWORD'],
    decode_responses=True
)

jw_token = JWTManager(app)

@jw_token.token_in_blacklist_loader
def check_invalid_token(token):
    jti = token['jti']
    registry = redis_db.get(jti)
    if registry is None:
        return True
    return registry == 'true'

@app.template_filter()
def date_custom_filter(value, format='%Y/%m/%d'):
    return value.strftime(format)

app.jinja_env.filters['customdate'] = date_custom_filter

    #return app