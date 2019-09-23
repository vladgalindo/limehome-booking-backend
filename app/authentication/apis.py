from app import api, redis_db, check_invalid_token
from app.authentication.models import login
from app.authentication.services import AuthorizationService
from app.common.generic_models import authorization_parser
from flask_jwt_extended import jwt_required, get_raw_jwt, get_jti
from flask_restplus import Namespace, Resource

authorization_api = Namespace('authorization', description="User Authorization")

authorization_service = AuthorizationService()

@authorization_api.route('/login')
class AuthorizationLogin(Resource):
    '''
    Authorization Login Api
    '''
    @authorization_api.expect(login)
    def post(self):
        '''
        Login
        :return:
        '''
        response = authorization_service.login_user(api.payload)
        return response


@authorization_api.expect(authorization_parser)
@authorization_api.route('/logout')
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
        raw_jti = get_raw_jwt()['jti']
        ttl = redis_db.ttl(raw_jti)
        redis_db.set(raw_jti, 'true', ttl)
        return {"status": 202, "sms": "Successful logout, hope to see again soon"}, 202


@authorization_api.route('/jwt-check')
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
        return {"is_invalid": is_invalid}, 200