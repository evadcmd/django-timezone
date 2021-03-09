import logging

from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse

# Create your views here.

def index(req):
    return render(req, 'index.html')

def now(req):
    now = timezone.now()
    return JsonResponse({
        'now': now.isoformat()
    })
