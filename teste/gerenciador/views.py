from django.shortcuts import render, redirect
from .models import Produto, Pedido
from .utils import calcular_relatorio_geral
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from decimal import Decimal
from django.db.models import Sum
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('/admin/')  # Redireciona para a página de administração se for um administrador
            elif user.groups.filter(name='Vendedores').exists():
                return redirect('vendedor_interface')  # Redireciona para a página do vendedor se for um vendedor
    return render(request, 'gerenciador/login.html')

@login_required
def vendedor_interface(request):
    produtos = Produto.objects.all()  # Obtém todos os produtos
    return render(request, 'gerenciador/vendedor_interface.html', {'produtos': produtos})

@login_required
def interface(request):
    produtos = Produto.objects.all()  # Obtém todos os produtos
    return render(request, 'gerenciador/interface.html', {'produtos': produtos})


def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'gerenciador/lista_produtos.html', {'produtos': produtos})

def lista_pedidos(request):
    pedidos_list = Pedido.objects.all().order_by('-data_pedido')
    paginator = Paginator(pedidos_list, 10)  # 10 itens por página

    page = request.GET.get('page')
    try:
        pedidos = paginator.page(page)
    except PageNotAnInteger:
        pedidos = paginator.page(1)
    except EmptyPage:
        pedidos = paginator.page(paginator.num_pages)

    return render(request, 'gerenciador/lista_pedidos.html', {'pedidos': pedidos})

def adicionar_produto(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        preco = Decimal(request.POST['preco'])  # Converta o valor para Decimal
        quantidade_estoque = int(request.POST['quantidade_estoque'])  # Converta o valor para int
        descricao = request.POST['descricao']
        produto = Produto.objects.create(nome=nome, preco=preco, quantidade_estoque=quantidade_estoque, descricao=descricao)
        return redirect('lista_produtos')
    return render(request, 'adicionar_produto.html')

def registrar_pedido(request):
    if request.method == 'POST':
        produto_id = request.POST['produto']
        quantidade = request.POST['quantidade']
        forma_pagamento = request.POST['forma_pagamento']  # Adiciona a captura da forma de pagamento
        produto = Produto.objects.get(id=produto_id)
        pedido = Pedido.objects.create(produto=produto, quantidade=quantidade, forma_pagamento=forma_pagamento)  # Salva a forma de pagamento
        pedido.save()
        return redirect('lista_pedidos')
    produtos = Produto.objects.all()
    return render(request, 'registrar_pedido.html', {'produtos': produtos})


def area_analise(request):
    relatorio = calcular_relatorio_geral()
    return render(request, 'gerenciador/area_analise.html', {'relatorio': relatorio})

def area_analise(request):
    # Calcular o produto mais vendido
    produto_mais_vendido = Pedido.objects.values('produto__nome').annotate(quantidade_vendida=Sum('quantidade')).order_by('-quantidade_vendida').first()
    # Calcular a quantidade vendida de cada produto
    produtos_quantidade_vendida = Pedido.objects.values('produto__nome').annotate(quantidade_vendida=Sum('quantidade')).order_by('-quantidade_vendida')

    relatorio = calcular_relatorio_geral()

    return render(request, 'gerenciador/area_analise.html', {
        'relatorio': relatorio,
        'produto_mais_vendido': produto_mais_vendido,
        'produtos_quantidade_vendida': produtos_quantidade_vendida
    })