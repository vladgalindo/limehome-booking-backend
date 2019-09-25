from pymongo.write_concern import WriteConcern
from mongoengine import *
from ..common.meta_doc import BaseDocument

#connect("mongodb://limehomeadmin:LIMErlaarl9@ds217078.mlab.com:17078/limehomebooking?retryWrites=false", alias="limehome_booking", port=17078)


class Users(DynamicDocument):
    # Make all these fields required, so that if we try to save a User instance
    # that lacks one of these fields, we'll get a ValidationError, which we can
    # catch and render as an error on a form.
    #
    # Use the email as the "primary key" (will be stored as `_id` in MongoDB).
    email = EmailField(required=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    password = StringField(required=True)
    is_active = BooleanField(default=False)
    metadata = EmbeddedDocumentField(BaseDocument)
    meta = {'collection': 'users'}