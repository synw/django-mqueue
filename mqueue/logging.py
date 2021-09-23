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
            "format": (
                "[%(asctime)s] %(levelname)s ",
                "[%(name)s.%(funcName)s:%(lineno)d] %(message)s",
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "devlog": {
            "level": "WARNING",
            "filters": ["require_debug_true"],
            "class": "mqueue.handlers.LogsDBHandler",
            "formatter": "verbose",
        },
        "prodlog": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "mqueue.handlers.LogsDBHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["devlog", "prodlog"],
            "propagate": True,
        },
    },
}
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    "formatters": {
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
    "formatters": {
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
