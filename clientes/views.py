from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm
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