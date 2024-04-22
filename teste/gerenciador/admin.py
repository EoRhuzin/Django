from django.contrib import admin
from django import forms
from .models import Produto, Pedido
from django.urls import path
from .views import relatorio_geral

"""class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['produto'].queryset = Produto.objects.all().values_list('nome', flat=True)"""

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'quantidade_estoque', 'descricao']

class PedidoAdmin(admin.ModelAdmin):
    #form = PedidoForm
    list_display = ['produto', 'quantidade', 'valor_total', 'forma_pagamento', 'data_pedido']

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Pedido, PedidoAdmin)


class MeuAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        meu_urls = [
            path('relatorio-geral/', self.admin_view(relatorio_geral), name='relatorio_geral'),
        ]
        return meu_urls + urls

'''admin_site = MeuAdminSite(name='admin')

admin.site = admin_site

admin.autodiscover()
admin.sites.site = admin_site'''

