from datetime import datetime
from app.core.bookings.booking_dto import BookingDTO
from app.core.common.email_service import send_mail
from app.core.common.date_tools import format_datetime
from app.core.bookings.booking_model import Bookings
from app.core.users.user_model import Users
from bson import ObjectId
from app.core.common.error_handler import error_handler
from mongoengine import DoesNotExist
import json

booking_fetch = BookingDTO.booking_fetch
booking_save = BookingDTO.booking_save


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
        # payload = custom_marshal(payload, booking_save, 'create')
        print("payload: {}".format(payload))
        user = Users.objects.get(_id=ObjectId(payload['user']))
        booking = Bookings(place_id=payload['place_id'], icon=payload['icon'], latitude=payload['latitude'],
                           longitude=payload['longitude'], href=payload['href'], vicinity=payload['vicinity'],
                           title=payload['title'], arrival=payload['arrival'], departure=payload['departure'],
                           guests=payload['guests'], room_type=payload['room_type'], user=user,
                           created_on=format_datetime(datetime.now(), "%Y-%m-%dT%H:%M:%S.%f%z"))
        booking.save()

        send_mail([user['email']], "LimeHome App New Booking", 'New Booking', 'booking_email.html',
                  {'id': str(booking['_id']), 'name': user['first_name'], 'title': payload['title'], 'vicinity': payload[
                      'vicinity'], 'arrival': datetime.strptime(payload['arrival'], "%Y-%m-%dT%H:%M:%S.%f%z")})


    def update_booking(self, id, user_id, payload):
        '''
        Update a booking
        :param id:
        :param payload:
        :return:
        '''
        try:
            booking = Bookings.objects.get(_id=ObjectId(id))
            print(payload)
            payload['place_id'] = booking['place_id']
            # payload = custom_marshal(payload, booking_save, 'update')
            user = Users.objects.get(_id=ObjectId(user_id))
            booking.save(title=payload['title'], arrival=payload['arrival'], departure=payload['departure'],
                     guests=payload['guests'], room_type=payload['room_type'], place_id=payload['place_id'], user=user)
            booking.save()
        except DoesNotExist as e:
            message = "The booking you are trying to modify belongs to a different user"
            error_handler(code=400, message=message, ui_status=True)


    def fetch_booking(self, id):
        '''
        Fetch a booking
        :param id:
        :return:
        '''
        try:
            booking = Bookings.objects.get(_id=ObjectId(id))
            return json.loads(booking.to_json())
        except DoesNotExist as e:
            message = "The booking you are were looking for was not found"
            error_handler(code=404, message=message, ui_status=True)


    def fetch_booking_by_place(self, id):
        '''
        Fetch a booking
        :param id:
        :return:
        '''
        booking = Bookings.objects(place_id=id, is_deleted=False)
        #print(booking.to_json())
        if booking.count() > 0:
            return json.loads(booking.to_json())
        else:
            message = "This place have no bookings yet"
            error_handler(code=404, message=message, ui_status=True)

    def fetch_booking_by_user(self, user_id):
        '''
        Fetch a booking
        :param user_id:
        :return:
        '''
        # count, registry = mongobase_obj.get(COLLECTIONS['BOOKINGS'], {"user": id, "meta.is_deleted": False})
        booking = Bookings.objects(user=user_id, is_deleted=False)
        if booking.count() > 0:
            return json.loads(booking.to_json())
        else:
            message = "This user haven't book anything yet"
            error_handler(code=404, message=message, ui_status=True)


    def soft_delete_booking(self, id, payload):
        """
        Soft deleting a booking
        :param payload:
        :return:
        """
        try:
            booking = Bookings.objects.get(_id=ObjectId(id))
            print(booking.to_json())
            payload['place_id'] = booking['place_id']
            booking(place_id=payload['place_id'], is_deleted=True)
            booking.save()
        except DoesNotExist as e:
            message = "The booking you are trying to delete was not found"
            error_handler(code=400, message=message, ui_status=True)
