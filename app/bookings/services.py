from app.common.constants import COLLECTIONS
from app.common.custom_marshal import custom_marshal
from app.bookings.models import booking, booking_save
from app.common.email_service import send_mail
from app.common.mongo_base import MongoBase
from bson import ObjectId
from flask import abort
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
            e = BadRequest("The booking you are trying to modify belongs to a different user")
            e.data = {'ui': True, 'status': 'error', 'sms': "The booking you are trying to modify belongs to a different user"}
            raise e


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
            e = NotFound("The booking you are were looking for was not found")
            e.data = {'ui': True, 'status': 'error', 'sms': "The booking you are were looking for was not found"}
            raise e

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
            e = NotFound("This place have no bookings yet")
            e.data = {'ui': True, 'status': 'error', 'sms': "This place have no bookings yet"}
            raise e

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
            e = NotFound("This user haven't book anything yet")
            e.data = {'ui': True, 'status': 'error', 'sms': "This user haven't book anything yet"}
            raise e


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