from flask_restplus import Namespace, fields, reqparse
from .date_tools import get_time
from mongoengine import *
from mongoengine import *


class BaseDocument(EmbeddedDocument):
    is_deleted = BooleanField(default=False)
    created_on = DateTimeField(default=get_time())
    updated_on = DateTimeField(default=get_time())
    created_by = StringField()
    updated_by = StringField()