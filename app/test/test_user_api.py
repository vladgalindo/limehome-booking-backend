import unittest
import json
from .generic_test import GenericTestCase
from flask_testing import TestCase


def get_users(self):
    return self.client.get(
        '/user/',
        content_type='application/json'
    )


class TestUserApis(GenericTestCase):

    def test_get_all_users(self):
        with self.client:
            user_response = get_users(self)
            response_data = json.loads(user_response.data.decode())
            self.assertEqual(user_response.status_code, 200)

if __name__ == '__main__':
    unittest.main()