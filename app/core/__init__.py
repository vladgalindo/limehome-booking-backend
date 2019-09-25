import os
from flask import Flask
from flask_cors import CORS
from flask_mail import Mail
from flask_mongoengine import MongoEngine

db = MongoEngine()
email = Mail()

def create_app(config_name='config.Development'):
    app = Flask(__name__)
    app.config.from_object(os.getenv('FLASK_ENVIRONMENT', config_name))
    CORS(app)
    try:
        db.init_app(app)
    except Exception as e:
        print(e)

    email.init_app(app)

    @app.template_filter()
    def date_custom_filter(value, format='%Y/%m/%d'):
        return value.strftime(format)

    app.jinja_env.filters['customdate'] = date_custom_filter

    return app