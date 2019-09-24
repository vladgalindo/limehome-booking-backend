from flask_restplus import Namespace, Resource
from app import api
from .models import user_request
from .services import UserService

users_api = Namespace('users', description='Users APIs')
userService = UserService()


@users_api.route('/')
class Users(Resource):
    '''
    Add Users
    '''

    @users_api.expect(user_request)
    def post(self):
        """
        :return:
        """
        userService.register_user(api.payload)
        return {'ui': True, 'status': 'success',  "sms": 'Way to go, you have sing up'}, 200


@users_api.route('/activate/<string:id>')
class UserActivate(Resource):
    """
    Activate User
    """
    def get(self, id):
        """
        Activate the User
        :param id:
        :return:
        """
        userService.activate_user(id)
        return {'ui': True, 'status': 'success',  "sms": "You're ready to go!, activation Successfully"}, 200
