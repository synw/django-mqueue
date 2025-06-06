import django
import os
from django.conf import settings
from django.core.management import call_command
from pathlib import Path
Path("urls.py").write_text("""\
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
"""
)
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
settings.configure(DEBUG=True, INSTALLED_APPS=[
  "django.contrib.contenttypes",
  "django.contrib.admin",
  "django.contrib.auth",
  "mqueue"
], DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': ':memory:',
  }
},
ROOT_URLCONF="urls") 
django.setup()
call_command("migrate")