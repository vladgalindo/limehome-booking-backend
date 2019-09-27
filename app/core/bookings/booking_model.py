from mongoengine import *
from bson import ObjectId
'''from ..common.meta_doc import MetadataDocument'''
from ..users.user_model import Users


class Bookings(DynamicDocument):
    _id = ObjectIdField(primary_key=True, required=True, default=ObjectId())
    place_id = StringField(required=True)
    icon = StringField(required=False)
    latitude = StringField(required=True)
    longitude = StringField(required=True)
    href = StringField(required=True)
    vicinity = StringField(required=True)
    title = StringField(required=True)
    arrival = StringField(required=True)
    departure = StringField(required=True)
    guests = IntField(required=False)
    room_type = StringField(required=True)
    user = ReferenceField(Users)
    is_deleted = BooleanField(default=False)
    created_on = StringField(required=False)
    meta = {'collection': 'bookings'}