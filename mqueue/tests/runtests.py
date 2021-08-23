#!/usr/bin/env python3
import glob
import os
import sys

import django
from django.conf import settings
from django.core.management import execute_from_command_line


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.abspath(os.path.join(BASE_DIR, "..")))

# Unfortunately, apps can not be installed via ``modify_settings``
# decorator, because it would miss the database setup.
CUSTOM_INSTALLED_APPS = (
    "mqueue",
    "django.contrib.admin",
    "graphene_django",
    "django_filters",
)

ALWAYS_INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
)

ALWAYS_MIDDLEWARE_CLASSES = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

TEMPLATES_DIR = BASE_DIR + "/templates"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


settings.configure(
    SECRET_KEY="django_tests_secret_key",
    DEBUG=False,
    TEMPLATES=TEMPLATES,
    TEMPLATE_DEBUG=False,
    ALLOWED_HOSTS=[],
    INSTALLED_APPS=ALWAYS_INSTALLED_APPS + CUSTOM_INSTALLED_APPS,
    MIDDLEWARE=ALWAYS_MIDDLEWARE_CLASSES,
    ROOT_URLCONF="tests.urls",
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "test_db",
        }
    },
    LANGUAGE_CODE="en-us",
    TIME_ZONE="UTC",
    USE_I18N=True,
    USE_L10N=True,
    USE_TZ=True,
    STATIC_URL="/static/",
    # Use a fast hasher to speed up tests.
    PASSWORD_HASHERS=("django.contrib.auth.hashers.MD5PasswordHasher",),
    FIXTURE_DIRS=glob.glob(BASE_DIR + "/" + "*/fixtures/"),
    MQUEUE_AUTOREGISTER=(("django.contrib.auth.models.User", ["c", "d", "u"]),),
    MQUEUE_HOOKS={
        "redis": {
            "path": "mqueue.hooks.redis",
            "host": "localhost",
            "port": 6379,
            "db": 0,
        },
    },
    GRAPHENE={"SCHEMA": "mqueue.schema.schema"},
    DEFAULT_AUTO_FIELD="django.db.models.BigAutoField",
)

django.setup()
args = [sys.argv[0], "test"]

# Current module (``tests``) and its submodules.
test_cases = "."

# Allow accessing test options from the command line.
offset = 1
try:
    sys.argv[1]
except IndexError:
    pass
else:
    option = sys.argv[1].startswith("-")
    if not option:
        test_cases = sys.argv[1]
        offset = 2

args.append(test_cases)
# ``verbosity`` can be overwritten from command line.
args.append("--verbosity=2")
args.extend(sys.argv[offset:])

print("ARFS", args)

# args = ["coverage run", 'test']
execute_from_command_line(args)
