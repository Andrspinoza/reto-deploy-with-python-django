import platform
import socket

import django
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone


def index(request):
    context = {
        "hostname": socket.gethostname(),
        "python_version": platform.python_version(),
        "django_version": django.get_version(),
        "server_time": timezone.localtime(),
        "scheme": request.scheme,
    }
    return render(request, "index.html", context)


def health(request):
    return JsonResponse({"status": "ok"})
