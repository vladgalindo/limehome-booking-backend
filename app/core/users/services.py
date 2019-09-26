from bson import ObjectId
from passlib.hash import argon2
from mongoengine import DoesNotExist

from app.core import app
from app.core.common.error_handler import error_handler
from app.core.common.email_service import send_mail
from .user_model import Users

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
            message = "Password are not the same"
            error_handler(code=400, message=message, ui_status=True)

        check_user = Users.objects(email=body['email'])
        if check_user.count() > 0:
            message = "Email belongs to another user"
            error_handler(code=400, message=message, ui_status=True)

        #body = custom_marshal(body, UserDTO.user, 'create')
        body['password'] = argon2.using(rounds=4).hash(body['password'])
        new_user = Users(email=body['email'], first_name=body['first_name'], last_name=body['last_name'], password=body['password'] )
        _id = new_user.save()
        link = app.config['ACTIVATION_URL'].format(id=_id, url_prefix=app.config['APP_URL_PREFIX'])
        # print(link)
        send_mail([body['email']], "LimeHome App Account Activation", link, 'activation_email.html',
                  {'link': link, 'name': body['first_name']})


    def activate_user(self, id):
        """
        Get the user activated
        :param id:
        :return:
        """
        try:
            check_user = Users.objects.get(_id=ObjectId(id))
            if check_user['is_active']:
                message = "Account Already Active"
                error_handler(code=400, message=message, ui_status=True)
            else:
                check_user.update(is_active=True)
        except DoesNotExist as e:
            message = "This Link is invalid"
            error_handler(code=400, message=message, ui_status=True)