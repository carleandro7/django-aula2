from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .models import Pedido
from .forms import ClienteForm
from .forms import PedidoForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

@login_required
def criar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/criar_cliente.html', {'form': form})

@login_required
def atualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/atualizar_cliente.html', {'form': form})

@login_required
def deletar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        cliente.delete()
        return redirect('listar_clientes')  # Redireciona para a lista de clientes
    return render(request, 'clientes/deletar_cliente.html', {'cliente': cliente})


@login_required
def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/lista_pedidos.html', {'pedidos': pedidos})

@login_required
def criar_pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'pedidos/criar_pedido.html', {'form': form})

@login_required
def atualizar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == "POST":
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'pedidos/atualizar_pedido.html', {'form': form})

@login_required
def deletar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == "POST":
        pedido.delete()
        return redirect('listar_pedidos')  # Redireciona para a lista de pedidos
    return render(request, 'pedidos/deletar_pedido.html', {'pedido': pedido})