import os
import unittest
import json
from app.test.generic_test import GenericTestCase
from app.core.users.user_model import Users
from app.test.mock_user_data import VALID_USER, INVALID_USER, ACTIVATED_USER


def save_users(self):
    return self.client.post(
        '/api/v1.0/users/',
        data=json.dumps(VALID_USER),
        content_type='application/json'
    )

def save_users_password_mismatch(self):
    return self.client.post(
        '/api/v1.0/users/',
        data=json.dumps(INVALID_USER),
        content_type='application/json'
    )

def error_saving_users(self):
    Users(email='example@gmail.com',
            first_name='username',
            last_name='username',
            password='123456',
            confirm_password= "123456").save()
    return self.client.post(
        '/api/v1.0/users/',
        data=json.dumps(VALID_USER),
        content_type='application/json'
    )

def activate_users(self):
    new_user = Users(email='example@gmail.com',
            first_name='username',
            last_name='username',
            password='123456',
            confirm_password= "123456").save()
    return self.client.get(
        '/api/v1.0/users/activate/{}'.format(str(new_user['_id'])),
        content_type='application/json'
    )

def error_activate_users(self):
    new_user = Users(email='example@gmail.com',
            first_name='username',
            last_name='username',
            password='123456',
            confirm_password= "123456",
            is_active=True).save()
    return self.client.get(
        '/api/v1.0/users/activate/{}'.format(str(new_user['_id'])),
        content_type='application/json'
    )


class TestUserApis(GenericTestCase):

    def test_save_users(self):
        with self.client:
            user_response = save_users(self)
            #response_data = json.loads(user_response.data.decode())
            self.assertEqual(user_response.status_code, 200)

    def test_activate_users(self):
        with self.client:
            user_response = activate_users(self)
            #response_data = json.loads(user_response.data.decode())
            self.assertEqual(user_response.status_code, 200)

    def test_error_saving_users(self):
        with self.client:
            user_response = error_saving_users(self)
            response_data = json.loads(user_response.data.decode())
            self.assertEqual(user_response.status_code, 400)

    def test_error_save_users_password_mismatch(self):
        with self.client:
            user_response = save_users_password_mismatch(self)
            response_data = json.loads(user_response.data.decode())
            self.assertEqual(user_response.status_code, 400)

    def test_error_activate_users(self):
        with self.client:
            user_response = error_activate_users(self)
            self.assertEqual(user_response.status_code, 400)


if __name__ == '__main__':
    unittest.main()