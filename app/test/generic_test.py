from flask_testing import TestCase
from app.core import db
from run import app
import unittest
from mongoengine import connect, disconnect, get_connection


class GenericTestCase(TestCase):

    def create_app(self):
        app.config.from_object('config.Testing')
        return app

    def setUp(self):
        connect(alias='testdb')
        conn = get_connection()

    def tearDown(self):
        disconnect()
