from app.common.constants import COLLECTIONS
from app.common.custom_marshal import custom_marshal
from app.bookings.models import booking, booking_save
from app.common.email_service import send_mail
from app.common.mongo_base import MongoBase
from bson import ObjectId
from app.common.error_handler import error_handler
from werkzeug.exceptions import BadRequest, NotFound

mongobase_obj = MongoBase()


class BookingService(object):
    '''
    Booking services
    '''

    def create_booking(self, payload):
        '''
        Register a new booking from a user
        :param payload:
        :return:
        '''
        payload = custom_marshal(payload, booking_save, 'create')
        _id = mongobase_obj.insert(COLLECTIONS['BOOKINGS'], payload)

        '''send_mail([body['email']], "LimeHome App Account Activation", link, 'activation_email.html',
                  {'link': link, 'name': body['first_name']})'''

    def update_booking(self, id, user_id, payload):
        '''
        Update a booking
        :param id:
        :param payload:
        :return:
        '''
        count, registry = mongobase_obj.get(COLLECTIONS['BOOKINGS'], {"user": user_id, "_id": ObjectId(id)})
        if count > 0:
            payload['place_id'] = registry[0]['place_id']
            payload = custom_marshal(payload, booking_save, 'update')
            mongobase_obj.update(COLLECTIONS['BOOKINGS'], {"_id": ObjectId(id)}, {"$set": payload})
        else:
            message = "The booking you are trying to modify belongs to a different user"
            error_handler(code=400, message=message, ui_status=True)


    def fetch_booking(self, id):
        '''
        Fetch a booking
        :param id:
        :return:
        '''
        count, registry = mongobase_obj.get(COLLECTIONS['BOOKINGS'], {"_id": ObjectId(id), "meta.is_deleted": False})
        if count > 0:
            return registry
        else:
            message = "The booking you are were looking for was not found"
            error_handler(code=404, message=message, ui_status=True)

    def fetch_booking_by_place(self, id):
        '''
        Fetch a booking
        :param id:
        :return:
        '''
        count, registry = mongobase_obj.get(COLLECTIONS['BOOKINGS'], {"place_id": id, "meta.is_deleted": False})
        if count > 0:
            return registry
        else:
            message = "This place have no bookings yet"
            error_handler(code=404, message=message, ui_status=True)

    def fetch_booking_by_user(self, id):
        '''
        Fetch a booking
        :param id:
        :return:
        '''
        count, registry = mongobase_obj.get(COLLECTIONS['BOOKINGS'], {"user": id, "meta.is_deleted": False})
        if count > 0:
            return registry
        else:
            message = "This user haven't book anything yet"
            error_handler(code=404, message=message, ui_status=True)


    def soft_delete_booking(self, id, payload):
        """
        Soft deleting a booking
        :param payload:
        :return:
        """
        payload = custom_marshal(payload, booking_save, 'delete')
        payload["meta"]["is_deleted"] = True
        mongobase_obj.update(COLLECTIONS['BOOKINGS'], {"_id": ObjectId(id)},
                        {"$set": payload})