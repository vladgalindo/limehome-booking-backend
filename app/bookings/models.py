from app import api
from app.common.generic_models import meta
from flask_restplus import fields

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
})

booking_save = api.inherit('booking_save', booking, {
    'user': fields.String(),
    'meta': fields.Nested(meta)
})

booking_fetch = api.inherit('booking_fetch', booking_save, {
    '_id': fields.String()
})

'''
{
        "position": [
          48.84234,
          2.34969
        ],
        "distance": 113,
        "title": "Young & Happy Hostel",
        "averageRating": 0.0,
        "category": {
          "id": "hotel",
          "title": "Hotel",
          "href": "https://places.cit.api.here.com/places/v1/categories/places/hotel?app_id=iw8thRxwHyaYmlzB4nL3&app_code=Jj1JJy-8n3nUWjXoZVA_Kg",
          "type": "urn:nlp-types:category",
          "system": "places"
        },
        "icon": "https://download.vcdn.cit.data.here.com/p/d/places2_stg/icons/categories/01.icon",
        "vicinity": "80 Rue Mouffetard<br/>75005 Paris",
        "having": [],
        "type": "urn:nlp-types:place",
        "href": "https://places.cit.api.here.com/places/v1/places/250u09tv-2107956d3a4d4dd4b748aa9461940d84;context=Zmxvdy1pZD1iNGIxOTQ1YS02ODJjLTVkMzUtYWNmNC01NTQ2YzQ5ZTdjZWJfMTU2ODk5ODg0MDQxN18wXzU0MTgmcmFuaz0w?app_id=iw8thRxwHyaYmlzB4nL3&app_code=Jj1JJy-8n3nUWjXoZVA_Kg",
        "id": "250u09tv-2107956d3a4d4dd4b748aa9461940d84",
        "alternativeNames": [
          {
            "name": "Young & Happy",
            "language": "en"
          },
          {
            "name": "Young & Happy Hotel Paris",
            "language": "en"
          },
          {
            "name": "Young And Happy Hostel",
            "language": "en"
          },
          {
            "name": "Young Happy Hostel",
            "language": "en"
          }
        ]
      }
'''