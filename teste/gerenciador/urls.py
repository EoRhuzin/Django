from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('vendedor/', views.vendedor_interface, name='vendedor_interface'),
    path('interface/', views.interface, name='interface'),
    path('adicionar_produto/', views.adicionar_produto, name='adicionar_produto'),
    path('registrar_pedido/', views.registrar_pedido, name='registrar_pedido'),
    path('lista_produtos/', views.lista_produtos, name='lista_produtos'),
    path('lista_pedidos/', views.lista_pedidos, name='lista_pedidos'),
     path('area_analise/', views.area_analise, name='area_analise'),
]
