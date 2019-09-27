import unittest
from app.core import app
from app import blueprint

# app = create_app()
app.register_blueprint(blueprint)
app.app_context().push()


def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    app.run()
