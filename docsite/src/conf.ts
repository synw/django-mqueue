const links: Array<{ href: string; name: string }> = [
  // { href: "/python", name: "Python api" },
];

// python runtime
const pipPackages = ["django", "django-mqueue", "sqlite3"];
const pyodidePackages = [];
const examplesExtension = "py";

async function loadHljsTheme(isDark: boolean) {
  if (isDark) {
    await import("highlight.js/styles/base16/material-darker.css")
  } else {
    await import("highlight.js/styles/stackoverflow-light.css")
  }
}

/** Import the languages you need for highlighting */
import hljs from 'highlight.js/lib/core';
import python from 'highlight.js/lib/languages/python';
//import bash from 'highlight.js/lib/languages/bash';
//import typescript from 'highlight.js/lib/languages/typescript';
//import xml from 'highlight.js/lib/languages/xml';
//import json from 'highlight.js/lib/languages/json';
hljs.registerLanguage('python', python);
//hljs.registerLanguage('typescript', typescript);
//hljs.registerLanguage('bash', bash);
//hljs.registerLanguage('html', xml);
//hljs.registerLanguage('json', json);

//import initCode from "@/assets/py/init.py?raw"
const initCode = `import django
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
call_command("migrate")`

const libName = "django-mqueue";
const libTitle = "Django Mqueue";
const repoUrl = "https://github.com/synw/django-mqueue";

export {
  libName,
  libTitle,
  repoUrl,
  pipPackages,
  examplesExtension,
  pyodidePackages,
  links,
  hljs,
  initCode,
  loadHljsTheme
}