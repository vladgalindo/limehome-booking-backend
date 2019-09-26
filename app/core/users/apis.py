from flask import request
from flask_restplus import Resource
from .services import UserService
from .user_dto import UserDTO
from .user_model import Users

api = UserDTO.api
user_request = UserDTO.generic_users
user_service = UserService()

@api.route('/')
class Users(Resource):
    '''
    Add Users
    '''
    @api.doc('list_of_registered_users')
    @api.expect(user_request)
    def post(self):
        '''
        Register a user
        :return:
        '''
        print(api.payload)
        user_service.register_user(body=api.payload)
        return {'ui': True, 'status': 'success',  "sms": 'Way to go, you have sing up'}, 200


@api.route('/activate/<string:id>')
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

        user_service.activate_user(id)
        return {'ui': True, 'status': 'success',  "sms": "You're ready to go!, activation Successfully"}, 200
