# Generated by Django 5.0.4 on 2024-04-21 20:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantidade_estoque', models.IntegerField()),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('valor_total', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('forma_pagamento', models.CharField(choices=[('dinheiro', 'Dinheiro'), ('pix', 'PIX'), ('cartao', 'Cartão')], default='dinheiro', max_length=10)),
                ('data_pedido', models.DateTimeField(auto_now_add=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerenciador.produto')),
            ],
        ),
    ]