import unittest
import json
from flask_testing import TestCase
from app import app


def register_user(self):
    return self.client.post(
        '/api/v1.0/users/',
        data=json.dumps(dict(
            email='joe@gmail.com',
            first_name='username',
            last_name='username',
            password='123456',
            confirm_password='123456'
        )),
        content_type='application/json'
    )


class TestAuthBlueprint(TestCase):
    def test_registration(self):
        """ Test for user registration """
        with app.client:
            response = register_user(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully registered.')
            self.assertTrue(data['Authorization'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
'''
# test_bucketlist.py
import unittest
import os
import json
from app import app

fake_token = "132qewasdzcx5efg"
login_route = '{url_prefix}/users/login'.format(url_prefix=app.config['APP_URL_PREFIX'])
mock = {
  "email": "vlad.galindo@gmail.com",
  "password": "12345"
}

class AuthTestCase(unittest.TestCase):
    """This class represents the bucketlist test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.bucketlist = mock
        self.login_route = '{url_prefix}/users/login'.format(url_prefix=app.config['APP_URL_PREFIX'])

        # binds the app to the current context
        with self.app.test_client() as c:
            rv = c.post(login_route, json={
                'username': 'flask', 'password': 'secret'
            })
            json_data = rv.get_json()
            print(rv)
            assert fake_token == json_data['token']
            # create all tables
            # db.create_all()


    def test_bucketlist_creation(self):
        """Test API can create a bucketlist (POST request)"""
        res = self.client().post(login_route, data=self.bucketlist)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Go to Borabora', str(res.data))

fake_token = "132qewasdzcx5efg"
login_route = '{url_prefix}/users/login'.format(url_prefix=app.config['APP_URL_PREFIX'])


@app.route(login_route)
def login():
    json_data = request.get_json()
    email = json_data['email']
    password = json_data['password']
    returv = c.post(login_route, json={
        'username': 'flask', 'password': 'secret'
    })
    json_data = rv.get_json()
    print(rv)
    assert fake_token == json_data['token']rn jsonify(t
    json_data = rv.get_json()
    print(rv)
    assert fake_token == json_data['token']oken=fake_token)


with app.test_client() as c:
    rv = c.post(login_route, json={
        'username': 'flask', 'password': 'secret'
    })
    json_data = rv.get_json()
    print(rv)
    assert fake_token == json_data['token']'''


'''if __name__ == '__main__':
    unittest.main()'''