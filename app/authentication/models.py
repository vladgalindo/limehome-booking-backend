from flask_restplus import fields
from app import api

login = api.model('login', {
    'email': fields.String(required=True, description="Users email"),
    'password': fields.String(required=True, description="Users password")
})
