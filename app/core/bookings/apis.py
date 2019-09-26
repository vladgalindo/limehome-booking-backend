from app.core.bookings.booking_dto import BookingDTO
from app.core.bookings.services import BookingService
from app.core.common.generic_dto import GenericDTO
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restplus import Namespace, Resource, marshal


api = BookingDTO.api
auth_parser = GenericDTO.authorization_parser
booking_fetch = BookingDTO.booking_fetch
booking = BookingDTO.booking
booking_service = BookingService()


@api.expect(auth_parser)
@api.route('')
class Bookings(Resource):
    '''
    Manage saving and fetching for booking objects
    '''
    @jwt_required
    @api.expect(booking)
    def post(self):
        '''
        Save a booking
        :return:
        '''
        user_id = get_jwt_identity()
        req_payload = api.payload
        req_payload['user'] = user_id
        booking_service.create_booking(req_payload)
        return {"ui": True, "status": "success", "sms": "Booking saved successfully"}, 200


@api.expect(auth_parser)
@api.route('/<string:id>')
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
        return {'ui': False, 'status': 'success',  "sms": "Booking found", "data": marshal(data, BookingDTO.booking_fetch)}, 200

    @jwt_required
    @api.expect(booking)
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
        return {"ui": True, "status": "success", "sms": "Booking updated successfully"}, 202


@api.expect(auth_parser)
@api.route('/delete/<string:id>')
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
        return {"ui": True, "status": "success", "sms": "Booking deleted successfully"}, 202


@api.expect(auth_parser)
@api.route('/by-place/<string:id>')
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
        return {"ui": False, "status": "success", "sms": "Bookings by Place", "data": marshal(data, BookingDTO.booking_fetch)}, 200


@api.expect(auth_parser)
@api.route('/by-user')
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
        return {"ui": False, "status": "success", "sms": "Bookings by Users", "data": marshal(data, BookingDTO.booking_fetch)}, 200