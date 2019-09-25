import unittest
from flask_jwt_extended import JWTManager
from app.core import create_app
from app import blueprint
from redis import StrictRedis

app = create_app()
app.register_blueprint(blueprint)
app.app_context().push()

# Redis
redis_db = StrictRedis(
    host=app.config['REDIS_HOST'],
    port=app.config['REDIS_PORT'],
    db=app.config['REDIS_DB'],
    password=app.config['REDIS_PASSWORD'],
    decode_responses=True
)

# JWT
jw_token = JWTManager(app)

@jw_token.token_in_blacklist_loader
def check_invalid_token(token):
    jti = token['jti']
    registry = redis_db.get(jti)
    if registry is None:
        return True
    return registry == 'true'


def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    app.run()
