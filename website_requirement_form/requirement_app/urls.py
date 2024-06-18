# requirement_app/urls.py
from django.urls import path
from .views import requirement_form_view

urlpatterns = [
    path('', requirement_form_view, name='requirement_form'),
]

