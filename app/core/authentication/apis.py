from app.core import check_invalid_token
from app.core.common.redis_db import redis_db
from app.core.authentication.auth_dto import AuthDTO
from app.core.authentication.services import AuthorizationService
from app.core.common.generic_dto import GenericDTO
from flask_jwt_extended import jwt_required, get_raw_jwt
from flask_restplus import Resource
from app.core.common.error_handler import error_handler

api = AuthDTO.api
login_dto = AuthDTO.login
auth_parser = GenericDTO.authorization_parser

authorization_service = AuthorizationService()

@api.route('/login')
class AuthorizationLogin(Resource):
    '''
    Authorization Login Api
    '''
    @api.expect(login_dto)
    def post(self):
        '''
        Login
        :return:
        '''
        response = authorization_service.login_user(api.payload)
        return response


@api.expect(auth_parser)
@api.route('/logout')
class AuthorizationLogout(Resource):
    '''
    Authorization Logout Api
    '''

    @jwt_required
    def post(self):
        '''
        Logout
        :return:
        '''
        try:
            raw_jti = get_raw_jwt()['jti']
            ttl = redis_db.ttl(raw_jti)
            redis_db.set(raw_jti, 'true', ttl)
            return {'ui': True, 'status': 'success', "sms": "Successful logout, hope to see again soon"}, 202
        except Exception as e:
            message = "Something weird happen, we will log you out anyway, just to make sure"
            error_handler(code=400, message=message, ui_status=True)


@api.route('/jwt-check')
class JwtValidation(Resource):
    '''
    Check JWT validation
    '''

    @jwt_required
    def post(self):
        '''
        Check JWT validation
        :param token:
        :return:
        '''
        is_invalid = check_invalid_token(get_raw_jwt())
        return {'ui': False, 'status': 'success',  "is_invalid": is_invalid}, 200