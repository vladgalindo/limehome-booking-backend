from mockupdb import go, MockupDB
import unittest
import datetime

# Our own database class using PyMongo
from app.common.mongo_base import MongoBase

BOOKING_DOC = {
      "_id": "5d85920ab0c4c7ef78a9f3c0",
      "user": "5d8450a0b96001a56e8717b4",
      "meta": {
        "is_deleted": False,
        "created_on": "2019-09-20T21:59:22.367000",
        "updated_on": "2019-09-20T21:59:22.367000",
        "created_by": "5d8450a0b96001a56e8717b4",
        "updated_by": "5d8450a0b96001a56e8717b4"
      },
      "place_id": "6046mc5p-eedbbf827b1e4d34b53e4e5333d1678d",
      "icon": "https://download.vcdn.cit.data.here.com/p/d/places2_stg/icons/categories/01.icon",
      "latitude": "-12.09394",
      "longitude": "-77.02646",
      "href": "https://places.cit.api.here.com/places/v1/places/6046mc5p-eedbbf827b1e4d34b53e4e5333d1678d;context=Zmxvdy1pZD1mM2JjZjM3Yi1hMjM2LTU5NmEtOGJmNS1iYzZjNmI5MDI0Y2FfMTU2OTAyMzU3ODk0Nl8wXzUwNjUmcmFuaz0w?app_id=iw8thRxwHyaYmlzB4nL3&app_code=Jj1JJy-8n3nUWjXoZVA_Kg",
      "vicinity": "Calle Andrés Reyes<br/>Jardín, San Isidro, 15046",
      "title": "Holiday Inn Express Lima San Isidro",
      "arrival": "2019-09-19T22:14:44.349000+00:00",
      "departure": "2019-09-22T22:14:44.349000+00:00",
      "guests": 2,
      "room_type": "suite"
    }


class MongoMockTest(unittest.TestCase):

    def setUp(self):
        self.server = MockupDB(auto_ismaster={"maxWireVersion": 3})
        self.server.run()
        print(self.server.uri)
        print(self.server)
        self.database = MongoBase(self.server.uri)

    def tearDown(self):
        self.server.stop()

    def test_list_booking(self):
        document = BOOKING_DOC

        document_query = go(self.database.get('BOOKING', {}))

        request = self.server.receives()

        # returns to pymongo a list containing only 1 the document
        request.reply([BOOKING_DOC])

        self.assertIsInstance(document_query()[0]['user'], str)
        self.assertEqual(
            document['user'],
            document_query()[0]['user']
        )

if __name__ == '__main__':
    unittest.main()