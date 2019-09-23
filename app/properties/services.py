import requests
from app import app


class PropertiesService(object):
    '''
    Properties BFF for https://developer.here.com APIs
    '''
    def get_hotels(self, location_type, lat, log):
        '''
        Fetch hotels from https://places.cit.api.here.com/places/v1/discover/explore
        :param location_type:
        :param lat:
        :param log:
        :return:
        '''
        response = requests.get(app.config['HERE_PLACES_URL'],
                                params={
                                    'app_id': app.config['HERE_APP_ID'],
                                    'app_code': app.config['HERE_APP_CODE'],
                                    location_type: '{},{};r=1500'.format(lat, log),
                                    'cat': 'hotel',
                                    'pretty': ''
                                })
        return response.json(), 200
