from pymongo.write_concern import WriteConcern
from mongoengine import *
from bson import ObjectId

class Users(DynamicDocument):
    _id = ObjectIdField(primary_key=True, required=True, default=ObjectId())
    email = EmailField(required=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    password = StringField(required=True)
    is_active = BooleanField(default=False)
    meta = {'collection': 'users'}