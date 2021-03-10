from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.django_template, name='django_template'),
    path('now', views.now)
]