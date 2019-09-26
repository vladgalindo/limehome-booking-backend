from app.core.common.generic_dto import GenericDTO
from app.core.properties.services import PropertiesService
from flask_restplus import Namespace, Resource
from flask_jwt_extended import jwt_required

properties_service = PropertiesService()
auth_parser = GenericDTO.authorization_parser
api = Namespace('properties', description='Properties APIs')


@api.expect(auth_parser)
@api.route('/hotels/<string:location_type>/<string:lat>/<string:log>')
class HotelList(Resource):
    @jwt_required
    def get(self, location_type, lat, log):
        return properties_service.get_hotels(location_type, lat, log)
