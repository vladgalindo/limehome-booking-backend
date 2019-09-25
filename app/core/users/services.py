import os
from  app.core.common.error_handler import error_handler
from  app.core.common.email_service import send_mail
from  app.core.common.custom_marshal import custom_marshal
from passlib.hash import argon2
from .user_dto import UserDTO
from .doc_model import Users

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

        check_user = Users.objects(email = body['email'])
        if check_user.count() > 0:
            message = "Email belongs to another user"
            error_handler(code=400, message=message, ui_status=True)

        body = custom_marshal(body, UserDTO.user, 'create')
        body['password'] = argon2.using(rounds=4).encrypt(body['password'], )
        new_user = Users(email=body['email'], first_name=body['first_name'], last_name=body['last_name'], password=body['password'] )
        _id = new_user.save()
        link = os.getenv('ACTIVATION_URL').format(id=_id, url_prefix=os.getenv('APP_URL_PREFIX'))
        # print(link)
        send_mail([body['email']], "LimeHome App Account Activation", link, 'activation_email.html',
                  {'link': link, 'name': body['first_name']})
