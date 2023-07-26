# cat_facts_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cat_facts, name='cat_facts'),
]
