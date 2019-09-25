import os
from flask_restplus import Api
from flask import Blueprint, url_for

from .core.users.apis import api as user_apis

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


@api.errorhandler(Exception)
def error_handler(err):
    error_code = err.code
    sms = err.__str__
    return {"error_code": error_code, "sms": sms}, error_code


api.add_namespace(user_apis, path='/api/v1.0/users/')