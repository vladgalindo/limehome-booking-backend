from app import api
from app.bookings.models import booking, booking_fetch
from app.bookings.services import BookingService
from app.common.generic_models import authorization_parser
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restplus import Namespace, Resource, marshal

booking_api = Namespace('bookings', description="Booking APIs")

booking_service = BookingService()


@booking_api.expect(authorization_parser)
@booking_api.route('')
class Bookings(Resource):
    '''
    Manage saving and fetching for booking objects
    '''
    @jwt_required
    @booking_api.expect(booking)
    def post(self):
        '''
        Save a booking
        :return:
        '''
        user_id = get_jwt_identity()
        req_payload = api.payload
        req_payload['user'] = user_id
        booking_service.create_booking(req_payload)
        return {"Status": "Booking saved successfully"}


@booking_api.expect(authorization_parser)
@booking_api.route('/<string:id>')
class BookingFetchUpdate(Resource):
    '''
    Fetch, Update bookings
    '''

    @jwt_required
    def get(self, id):
        '''
        Fetch a booking
        :param id:
        :return:
        '''
        data = booking_service.fetch_booking(id)
        return {"Status": "Booking found", "data": marshal(data, booking_fetch)}

    @jwt_required
    @booking_api.expect(booking)
    def put(self, id):
        '''
        Update a booking
        :param id:
        :return:
        '''
        user_id = get_jwt_identity()
        req_payload = api.payload
        req_payload['user'] = user_id
        booking_service.update_booking(id, user_id, req_payload)
        return {"Status": "Booking updated successfully"}


@booking_api.expect(authorization_parser)
@booking_api.route('/delete/<string:id>')
class BookingDelete(Resource):
    """
    Delete Booking
    """
    @jwt_required
    def delete(self, id):
        """
        Delete Booking
        :param id:
        :return:
        """
        user_id = get_jwt_identity()
        req_payload = api.payload
        req_payload['user'] = user_id
        booking_service.soft_delete_booking(id, req_payload)
        return {'Message': "Booking deleted successfully"}


@booking_api.expect(authorization_parser)
@booking_api.route('/by-place/<string:id>')
class BookingsByPlace(Resource):
    """
    Fetch bookings by place
    """
    @jwt_required
    def get(self, id):
        '''
        Fetch a booking by place
        :param id:
        :return:
        '''
        data = booking_service.fetch_booking_by_place(id)
        return {"Status": "Bookings by Place", "data": marshal(data, booking_fetch)}


@booking_api.expect(authorization_parser)
@booking_api.route('/by-user')
class BookingsByUser(Resource):
    """
    Fetch bookings by logged user
    """
    @jwt_required
    def get(self):
        '''
        Fetch a booking by logged user
        :param id:
        :return:
        '''
        user_id = get_jwt_identity()
        data = booking_service.fetch_booking_by_user(user_id)
        return {"Status": "Bookings by Users", "data": marshal(data, booking_fetch)}