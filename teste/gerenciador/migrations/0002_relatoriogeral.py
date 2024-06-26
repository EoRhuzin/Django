# Generated by Django 5.0.4 on 2024-04-21 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatorioGeral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_total_vendas', models.IntegerField(default=0)),
                ('total_dinheiro_geral', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_pix', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_dinheiro', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_cartao', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
    ]
