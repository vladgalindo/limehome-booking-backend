import os
import unittest

from flask import current_app
from flask_testing import TestCase

from run import app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object(os.getenv('config.Development'))
        return app

    def test_development_environment(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'piece_of_cake')
        print(type(app.config['DEBUG']))
        self.assertTrue(app.config['DEBUG'])
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['DB_HOST'] == 'ds217078.mlab.com'
        )

class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('config.Testing')
        return app

    def test_testing_environment(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'piece_of_cake')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['DB_HOST'] == 'ds047037.mlab.com'
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('config.Production')
        return app

    def test_production_environment(self):
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()