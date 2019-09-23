import logging
from logging import config

LOG_CONFIG = {
    "version": 1,
    "formatters": {
        "json": {
            "()": "flask_google_cloud_logger.FlaskGoogleCloudFormatter",
            "application_info": {
                "type": "python-application",
                "application_name": "Example Application"
            },
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
        }
    },
    "handlers": {
        "json": {
            "class": "logging.StreamHandler",
            "formatter": "json"
        }
    },
    "loggers": {
        "root": {
            "level": "INFO",
            "handlers": ["json"]
        },
        "werkzeug": {
            "level": "WARN",  # Disable werkzeug hardcoded logger
            "handlers": ["json"]
        }
    }
}

config.dictConfig(LOG_CONFIG)  # load log config from dict
logger = logging.getLogger("root")  # get root logger instance