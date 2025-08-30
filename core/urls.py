# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('clientes/', views.cliente_list_view, name='cliente_list'),
    path('api/clientes/', views.listar_clientes, name='api_clientes'),
    path('clientes/novo/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('clientes/editar/', views.atualizar_cliente, name='atualizar_cliente'),
    path('clientes/deletar/', views.deletar_cliente, name='deletar_cliente'),

    path('funcionarios/', views.funcionario_list_view, name='listar_funcionarios'),
    path('api/funcionarios/', views.listar_funcionarios, name='api_funcionarios'),
    path('funcionario/novo/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('funcionario/editar/', views.atualizar_funcionario, name='atualizar_funcionario'),
    path('funcionario/deletar/', views.deletar_funcionario, name='deletar_funcionario'),

   
]