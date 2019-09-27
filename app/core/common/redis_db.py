import config
from redis import StrictRedis
from app.core import app

# Redis
redis_db = StrictRedis(
    host=app.config['REDIS_HOST'],
    port=app.config['REDIS_PORT'],
    db=app.config['REDIS_DB'],
    password=app.config['REDIS_PASSWORD'],
    decode_responses=True
)