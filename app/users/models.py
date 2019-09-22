from flask_restplus import fields
from app.common.generic_models import meta
from app import api


generic_users = api.model('singup', {
    'email': fields.String(description="Email"),
    'first_name': fields.String(description="First Name"),
    'last_name': fields.String(description="Last Name"),
    'password': fields.String(description="Password")
})

user = api.inherit('user', generic_users, {
    'is_active': fields.Boolean(default=False, description="Is account Activated"),
    'meta': fields.Nested(meta)
})

user_request = api.inherit('generic users', generic_users, {
    'confirm_password': fields.String(description="Confirm password")
})