import logging

from django.shortcuts import render
from django.utils import timezone, dateformat
from django.http import JsonResponse

from .models import Log

# Create your views here.

logging.basicConfig(level=logging.INFO)
TIME_FMT = '%Y-%m-%d %H:%M:%S'

def index(req):
    return render(req, 'index.html')

def now(req):
    now = timezone.now()
    Log.objects.create().save()
    return JsonResponse({
        'now': now.isoformat()
    })

def django_template(req):
    now = timezone.now()
    Log.objects.create().save()
    return render(
        req,
        'django_template.html',
        {'now': timezone.localtime(now).strftime(TIME_FMT)}
    )

