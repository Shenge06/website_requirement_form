# requirements/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.website_requirement_form, name='website_requirement_form'),
    path('success/', views.success_view, name='success'),
]
