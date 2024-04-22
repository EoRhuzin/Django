from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    quantidade_estoque = models.IntegerField()
    descricao = models.TextField()

class Pedido(models.Model):
    FORMA_PAGAMENTO_CHOICES = [
        ('dinheiro', 'Dinheiro'),
        ('pix', 'PIX'),
        ('cartao', 'Cartão'),
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    valor_total = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    forma_pagamento = models.CharField(max_length=10, choices=FORMA_PAGAMENTO_CHOICES, default='dinheiro')
    data_pedido = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.valor_total = self.produto.preco * self.quantidade
        super().save(*args, **kwargs)

    def __str__(self):
        return self.produto.nome

