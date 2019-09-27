import os
from flask_restplus import Api
from flask import Blueprint, url_for

from .core.users.apis import api as user_apis
from .core.properties.apis import api as properties_apis
from .core.authentication.apis import api as auth_apis
from .core.bookings.apis import api as booking_apis
from app.core import app

blueprint = Blueprint('api', __name__)
if os.getenv('FLASK_ENVIRONMENT') == "config.Production":
    @property
    def specs_url(self):
        return url_for(self.endpoint('specs'), _external=True, _scheme='https')

    Api.specs_url = specs_url


api = Api(blueprint,
          title='LimeHome Booking App', description='LimeHome App',
          version='1.0',
          )

api.add_namespace(user_apis, '{url_prefix}/users'.format(url_prefix=app.config['APP_URL_PREFIX']))
api.add_namespace(properties_apis, '{url_prefix}/properties'.format(url_prefix=app.config['APP_URL_PREFIX']))
api.add_namespace(auth_apis, '{url_prefix}/auth'.format(url_prefix=app.config['APP_URL_PREFIX']))
api.add_namespace(booking_apis, '{url_prefix}/booking'.format(url_prefix=app.config['APP_URL_PREFIX']))


@api.errorhandler(Exception)
def error_handler(err):
    error_code = err.code
    sms = err.__str__
    return {"error_code": error_code, "sms": sms}, error_code