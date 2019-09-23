from app.common.generic_models import authorization_parser
from app.properties.services import PropertiesService
from flask_restplus import Namespace, Resource
from flask_jwt_extended import jwt_required

properties_service = PropertiesService()

properties_api = Namespace('properties', description='Properties APIs')


@properties_api.expect(authorization_parser)
@properties_api.route('/hotels/<string:location_type>/<string:lat>/<string:log>')
class HotelList(Resource):
    @jwt_required
    def get(self, location_type, lat, log):
        return properties_service.get_hotels(location_type, lat, log)
