from django.shortcuts import render, redirect
from .models import Produto, Pedido
from .utils import calcular_relatorio_geral

def adicionar_produto(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        tamanho = request.POST['tamanho']
        preco = request.POST['preco']
        produto = Produto.objects.create(nome=nome, tamanho=tamanho, preco=preco)
        produto.save()
        return redirect('lista_produtos')
    return render(request, 'adicionar_produto.html')

def registrar_pedido(request):
    if request.method == 'POST':
        produto_id = request.POST['produto']
        quantidade = request.POST['quantidade']
        produto = Produto.objects.get(id=produto_id)
        pedido = Pedido.objects.create(produto=produto, quantidade=quantidade)
        pedido.save()
        return redirect('lista_pedidos')
    produtos = Produto.objects.all()
    return render(request, 'registrar_pedido.html', {'produtos': produtos})

def relatorio_geral(request):
    relatorio = calcular_relatorio_geral()
    return render(request, 'admin/relatorio_geral.html', {'relatorio': relatorio})