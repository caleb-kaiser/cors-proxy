"""
URLs for cors_proxy.
"""
from django.urls import path 
from .views import cors_proxy

urlpatterns = [
    path('api/cors-proxy/', cors_proxy, name='cors_proxy'),
]
