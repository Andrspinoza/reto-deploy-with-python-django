"""Configuración mínima: una sola página, sin base de datos."""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# En el servidor estos valores llegan por variables de entorno, no del código.
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "solo-para-desarrollo-local")
DEBUG = os.environ.get("DJANGO_DEBUG", "0") == "1"
ALLOWED_HOSTS = [
    h.strip()
    for h in os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")
    if h.strip()
]

INSTALLED_APPS = ["home"]

MIDDLEWARE = ["django.middleware.security.SecurityMiddleware"]

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": False,
        "OPTIONS": {"context_processors": []},
    }
]

# Sin modelos no hace falta base de datos.
DATABASES = {}

# Nginx termina HTTPS y reenvía a Gunicorn por HTTP; este header le dice a
# Django que la petición original sí era segura.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

LANGUAGE_CODE = "es"
TIME_ZONE = "America/Lima"
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
