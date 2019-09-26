from passlib.hash import argon2
from flask_jwt_extended import create_access_token, create_refresh_token, get_jti
from mongoengine import DoesNotExist

from app.core.common.error_handler import error_handler
from app.core.common.redis_db import redis_db
from app.core import app
from app.core.users.user_model import Users


class AuthorizationService(object):
    '''
    Authorization management service
    '''

    def login_user(self, body):
        '''
        User login to retrieve jwt tokens
        :param body:
        :return:
        '''
        email, password = body['email'], body['password']
        try:
            user = Users.objects.get(email=email)  # "meta.is_deleted"
            if argon2.verify(password, user['password']):
                if user['is_active'] is True:
                    user_id = str(user['_id'])
                    access_token = create_access_token(identity=user_id)
                    refresh_token = create_refresh_token(identity=user_id)
                    access_jti = get_jti(encoded_token=access_token)
                    refresh_jti = get_jti(encoded_token=refresh_token)
                    redis_db.set(access_jti, 'false', app.config['JWT_ACCESS_TOKEN_EXPIRES'])
                    redis_db.set(refresh_jti, 'false', app.config['JWT_REFRESH_TOKEN_EXPIRES'])
                    return {"status": 202, "access_token": access_token, "refresh_token": refresh_token}, 202
                else:
                    message = "You are missing one step on your activation process, Please check your email for instruction to activate your user"
                    error_handler(code=401, message=message, ui_status=True)

            else:
                message = "Your Credentials don't match with our registries"
                error_handler(code=401, message=message, ui_status=True)
        except DoesNotExist as e:
            message = "Your Credentials don't match with our registries"
            error_handler(code=401, message=message, ui_status=True)
