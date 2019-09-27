from flask_mongoengine import MongoEngine
from flask_testing import TestCase
from app.core import db
from run import app
import unittest
from app.core.users.user_model import Users
from app.core.bookings.booking_model import Bookings
from mongoengine import connect, disconnect, get_connection


class GenericTestCase(TestCase):

    def create_app(self):
        app.config.from_object('config.Testing')
        return app

    def setUp(self):
        connect(alias='testdb')
        conn = get_connection()

    def tearDown(self):
        delete_users = Users.objects.all()
        for user in delete_users:
            Users.delete(user)
        delete_bookings = Bookings.objects.all()
        for booking in delete_bookings:
            Bookings.delete(booking)
