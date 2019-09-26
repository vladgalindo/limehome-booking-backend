from flask_restplus import Namespace, fields


class AuthDTO:
    api = Namespace('authorization', description="User Authorization")
    login = api.model('login', {
        'email': fields.String(required=True, description="Users email"),
        'password': fields.String(required=True, description="Users password")
    })
