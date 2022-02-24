# ====================================== Logs ============================
DEV_LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    "formatters": {
        "verbose": {
            "format": "{asctime} {levelname} {name} {funcName:s} {lineno:d} {message}",
            "style": "{",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "db": {
            "level": "WARNING",
            "filters": ["require_debug_true"],
            "class": "mqueue.handlers.LogsDBHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["db"],
            "propagate": False,
        },
    },
}
"""
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    "formatter": {
        "verbose": {
            "format": (
                "[%(asctime)s] %(levelname)s ",
                "[%(name)s.%(funcName)s:%(lineno)d] %(message)s",
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "prodlog": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "mqueue.handlers.LogsDBHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["prodlog"],
            "propagate": True,
        },
    },
}
LOGGING_WARNING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    "formatter": {
        "verbose": {
            "format": (
                "[%(asctime)s] %(levelname)s ",
                "[%(name)s.%(funcName)s:%(lineno)d] %(message)s",
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "prodlog": {
            "level": "WARNING",
            "filters": ["require_debug_false"],
            "class": "mqueue.handlers.LogsDBHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["prodlog"],
            "propagate": True,
        },
    },
}
"""
