# reto-deploy-with-python-django

Aplicación web mínima en **Django** servida con **Gunicorn** detrás de **Nginx**,
con HTTPS mediante **Certbot**.

```
Usuario → IP/dominio → Nginx (80/443) → Gunicorn (127.0.0.1:8000) → Django
```

## Estructura

```
manage.py                 # utilidad de Django
config/                   # proyecto: settings, urls, wsgi
home/                     # app: vistas y rutas
templates/index.html      # página principal
requirements.in           # dependencias principales (las que decidimos)
requirements.txt          # versiones exactas (generado desde el .in)
```

## Correr en local

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

## Correr como en producción

```bash
.venv/bin/gunicorn config.wsgi:application --bind 127.0.0.1:8000
```

Variables de entorno que lee la app:

| Variable | Para qué | Por defecto |
|---|---|---|
| `DJANGO_SECRET_KEY` | Clave secreta de Django | valor de desarrollo |
| `DJANGO_DEBUG` | `1` activa el modo debug | `0` |
| `DJANGO_ALLOWED_HOSTS` | Hosts permitidos, separados por coma | `localhost,127.0.0.1` |

## Regenerar `requirements.txt`

```bash
pip install pip-tools
pip-compile requirements.in -o requirements.txt
```
