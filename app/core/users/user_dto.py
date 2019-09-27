from flask_restplus import Namespace, fields


class UserDTO:
    api = Namespace('user', description='user related operations')
    generic_users = api.model('user', {
        'email': fields.String(required=True, description="Email"),
        'first_name': fields.String(required=True, description="First Name"),
        'last_name': fields.String(required=True, description="Last Name"),
        'password': fields.String(required=True, description="Password")
    })

    user = api.inherit('user', generic_users, {
        'is_active': fields.Boolean(default=False, description="Is account Activated")
    })

    user_request = api.inherit('generic users', generic_users, {
        'confirm_password': fields.String(description="Confirm password")
    })
