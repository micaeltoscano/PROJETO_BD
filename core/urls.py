# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clientes/', views.cliente_list_view, name='cliente_list'),
    path('api/clientes/', views.listar_clientes, name='api_clientes'),
    # ... outras APIs ...
]