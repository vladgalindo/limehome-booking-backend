import os
import unittest

from flask import current_app
from flask_testing import TestCase

from run import app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object(os.getenv('config.Development'))
        return app

    def test_app_is_development(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['DB_HOST'] == 'ds217078.mlab.com'
        )

class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('config.Testing')
        return app

    def test_app_is_testing(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['DB_HOST'] == 'ds217078.mlab.com'
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('config.Production')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()