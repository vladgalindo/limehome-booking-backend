from flask import abort
from bson import ObjectId
from passlib.hash import argon2
from werkzeug.exceptions import BadRequest

from app.users.models import user
from app.common.mongo_base import MongoBase
from app.common.email_service import send_mail
from app.common.custom_marshal import custom_marshal
from app.common.constants import COLLECTIONS
from app import app

mongobase_obj = MongoBase()


class UserService(object):
    """
    Service Class for User API
    """

    def register_user(self, body):
        """
        signup function
        :return:
        """
        if body.get('password') != body.get('confirm_password'):
            e = BadRequest("Password are not the same")
            e.data = {'ui': True, 'status': 'error',
                      'sms': "Password are not the same"}
            raise e

        count, records = mongobase_obj.get(COLLECTIONS['USERS'], {"email": body['email']})
        if count > 0:
            e = BadRequest("Email belongs to another user")
            e.data = {'ui': True, 'status': 'error',
                      'sms': "Email belongs to another user"}
            raise e

        body = custom_marshal(body, user, 'create')
        body['password'] = argon2.using(rounds=4).encrypt(body['password'], )
        _id = mongobase_obj.insert(COLLECTIONS['USERS'], body)
        link = app.config['ACTIVATION_URL'].format(id=_id, url_prefix=app.config['APP_URL_PREFIX'])
        # print(link)
        send_mail([body['email']],"LimeHome App Account Activation", link, 'activation_email.html', {'link': link, 'name': body['first_name']})

    def activate_user(self, id):
        """
        Get the user activated
        :param id:
        :return:
        """
        count, records = mongobase_obj.get(COLLECTIONS['USERS'], {"_id": ObjectId(id)})
        if count == 0:
            e = BadRequest("This Link is invalid")
            e.data = {'ui': True, 'status': 'error',
                      'sms': "This Link is invalid"}
            raise e
        if records[0]['is_active']:
            e = BadRequest("Account Already Active")
            e.data = {'ui': True, 'status': 'error',
                      'sms': "Account Already Active"}
            raise e
        else:
            mongobase_obj.update(COLLECTIONS['USERS'], {"_id": ObjectId(id)}, {"$set": {"is_active": True}})