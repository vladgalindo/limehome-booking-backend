from flask_restplus import fields, reqparse
from app import api
from .date_tools import get_time

meta = api.model('meta', {
    'is_deleted': fields.Boolean(default=False),
    'created_on': fields.DateTime(default=get_time()),
    'updated_on': fields.DateTime(default=get_time()),
    'created_by': fields.String(default='user'),
    'updated_by': fields.String(default='user')
})

authorization_parser = reqparse.RequestParser()
authorization_parser.add_argument('Authorization', location='headers')