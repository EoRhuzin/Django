from .models import Pedido
from django.db.models import Sum

def calcular_relatorio_geral():
    # Calcula a quantidade total de vendas
    quantidade_total_vendas = Pedido.objects.count()

    # Calcula a soma total de todos os valores
    soma_total = Pedido.objects.aggregate(soma_total=Sum('valor_total'))['soma_total'] or 0

    # Calcula a soma dos valores separados por método de pagamento
    soma_pix = Pedido.objects.filter(forma_pagamento='pix').aggregate(soma_pix=Sum('valor_total'))['soma_pix'] or 0
    soma_dinheiro = Pedido.objects.filter(forma_pagamento='dinheiro').aggregate(soma_dinheiro=Sum('valor_total'))['soma_dinheiro'] or 0
    soma_cartao = Pedido.objects.filter(forma_pagamento='cartao').aggregate(soma_cartao=Sum('valor_total'))['soma_cartao'] or 0

    return {
        'quantidade_total_vendas': quantidade_total_vendas,
        'soma_total': soma_total,
        'soma_pix': soma_pix,
        'soma_dinheiro': soma_dinheiro,
        'soma_cartao': soma_cartao
    }
