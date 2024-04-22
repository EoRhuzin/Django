from django.urls import path
from . import views
from .views import relatorio_geral
from django.urls import path, include

urlpatterns = [
    path('adicionar_produto/', views.adicionar_produto, name='adicionar_produto'),
    path('registrar_pedido/', views.registrar_pedido, name='registrar_pedido'),
    path('relatorio_geral/', views.relatorio_geral, name='relatorio_geral'),
]
