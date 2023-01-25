import logging

from logging.config import dictConfig

LOGGING_LEVEL = logging.DEBUG
FORMAT = "%(asctime)s %(name)s %(levelname)s: %(message)s"

logging_config = {
    "version": 1,
    "formatters": {
        "default": {
            "format": FORMAT, 
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    "handlers": {
        "console": {
            "level": logging.DEBUG,
            "class": "logging.StreamHandler",
            "formatter": "default",
            "stream": "ext://sys.stdout"
        },
        "file": {
            "level": logging.DEBUG,
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "default",
            "filename": "all.log",
            "maxBytes": 1024 * 1024,
            "backupCount": 3
        }
    },
    "loggers": {
        "": {
            "level": LOGGING_LEVEL,
            "handlers": ["console", "file"]
        },
    },
    "disable_existing_loggers": False
}

dictConfig(logging_config)

logger = logging.getLogger(__name__)