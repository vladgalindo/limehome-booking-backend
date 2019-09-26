from flask_restplus import Namespace
from flask_restplus import fields


class BookingDTO:
    api = Namespace('bookings', description="Booking APIs")
    booking = api.model('booking', {
        'place_id': fields.String(required=True, description="Place ID"),
        'icon': fields.String(required=False, description="Place icon"),
        'latitude': fields.String(required=True, description="Place latitude"),
        'longitude': fields.String(required=True, description="Place longitude"),
        'href': fields.String(required=True, description="Place href"),
        'vicinity': fields.String(required=True, description="Place vicinity"),
        'title': fields.String(required=True, description="Place title"),
        'arrival': fields.DateTime(required=True, description="Booking arrival date"),
        'departure': fields.DateTime(required=True, description="Booking departure date"),
        'guests': fields.Integer(required=False, description="Booking guests amount"),
        'room_type': fields.String(required=True, description="Booking room type"),
        'is_deleted': fields.Boolean(required=True, description="Booking room type"),
        'created_on': fields.DateTime(required=True, description="Booking creation date"),
    })

    booking_save = api.inherit('booking_save', booking, {
        'user': fields.String()
    })

    booking_fetch = api.inherit('booking_fetch', booking_save, {
        '_id': fields.String()
    })
