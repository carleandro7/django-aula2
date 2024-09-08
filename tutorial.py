#django-admin startproject  nomeprojeto
#python manage.py startapp nomeaplicacao


#python manage.py makemigrations 
#python manage.py migrate  
#python manage.py createsuperuser  
#python manage.py runserver  


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nomeaplicacao', #nome da aplicação criada
]



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'aula1bd',        # Nome do seu banco de dados
        'USER': 'postgres',     # Seu usuário do PostgreSQL
        'PASSWORD': 'postgres',   # Senha do usuário do PostgreSQL
        'HOST': 'localhost',     # endereço do seu servidor PostgreSQL
        'PORT': '5432',          # Porta padrão do PostgreSQL
    }
}

#para aplicação ficar em portugues

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

#pasta do template
STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'templates/static'),)



#exemplo de modelo com relacionamento e caracteres

from django.db import models

# Create your models here.
class Cliente(models.Model):
    matricula = models.CharField(max_length=20, unique=True) 
    nome = models.CharField(max_length=100) 
    cpf = models.CharField(max_length=11, unique=True) 

    def __str__(self): 
        return self.nome

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self): 
        return f"{self.descricao} - {self.valor}"



#registrando o modelo para o admin
from .models import Cliente, Pedido

admin.site.register(Cliente)
admin.site.register(Pedido)


#adicionar as urls da aplicação cliente ao projeto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes', include('clientes.urls')),
]


#criar a url de clientes 
from . import views

urlpatterns = [
    path('', views.listar_clientes, name='listar_clientes'),
    path('novo/', views.criar_cliente, name='criar_cliente'),
    path('editar/<int:id>/', views.atualizar_cliente, name='atualizar_cliente'),
    path('deletar/<int:id>/', views.deletar_cliente, name='deletar_cliente'),
]


###views.py de cliente com os metodos de cada pagina
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm
# Create your views here.

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def criar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/criar_cliente.html', {'form': form})


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

def deletar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        cliente.delete()
        return redirect('listar_clientes')  # Redireciona para a lista de clientes
    return render(request, 'clientes/deletar_cliente.html', {'cliente': cliente})



###form para criar o cliente

from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf']


##o arquivo base.html antes dele dentro da pasta template deve criar as pastas css e js. Respectivamente dentro destas pasta os arquivos base.css e base.js
{% load static %}
<!doctype html>
<html lang="pt-BR">
  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link rel="stylesheet" href="{% static 'css/base.css' %}">
    <title>Sistema Aula</title>
  </head>
  <body>
    <div class="sidebar">
    

        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
            <div class="container-fluid">
              <a class="navbar-brand" href="#">Sistema</a>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                  <li class="nav-item">
                    <a class="nav-link active"  href="{% url 'listar_clientes' %}">Clientes</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link active" href="#">Pedidos</a>
                  </li>
                 
                </ul>
              </div>
            </div>
          </nav>
      </div>
      
      <div class="container">
          {% block 'dashboard'%}
  
          {% endblock %}

      </div>


    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="{% static 'js/base.js' %}"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
    -->
  </body>
</html>


##o arquivo de listar os clientes
{% extends "base.html" %}
{% load static %}
{% block 'dashboard' %}
<h1>Lista de clientes</h1>
<a href="{% url 'criar_cliente' %}">Adicionar cliente</a>
<ul>
  {% for cliente in clientes %}
    <li>{{ cliente.nome }} - {{ cliente.cpf }}
      <a href="{% url 'atualizar_cliente' cliente.id %}">Editar</a> |
      <a href="{% url 'deletar_cliente' cliente.id %}">Deletar</a>
    </li>
  {% endfor %}
</ul>

{% endblock %}


##o arquivo de criar o cliente

<h1>Criar Cliente</h1>
<form method="post">
    {% csrf_token %}
    <div>
        <label for="id_nome">Nome:</label>
        <input type="text" id="id_nome" name="nome" value="{{ form.nome.value|default_if_none:'' }}" maxlength="100"
            required>
        {% if form.nome.errors %}
        <div class="error">{{ form.nome.errors }}</div>
        {% endif %}
    </div>

    <div>

        <label for="id_cpf">CPF:</label>
        <input type="text" id="id_cpf" name="cpf" value="{{ form.cpf.value|default_if_none:'' }}" maxlength="11"
            required>
        {% if form.cpf.errors %}
        <div class="error">{{ form.cpf.errors }}</div>
        {% endif %}
    </div>

    <button type="submit">Salvar</button>
</form>
<a href="{% url 'listar_clientes' %}">Voltar</a>


### o arquivo de atualizar o cliente
<h1>Atualizar Cliente</h1>
<form method="post">
    {% csrf_token %}
    <div>
        <label for="id_nome">Nome:</label>
        <input type="text" id="id_nome" name="nome" value="{{ form.nome.value|default_if_none:'' }}" maxlength="100"
            required>
        {% if form.nome.errors %}
        <div class="error">{{ form.nome.errors }}</div>
        {% endif %}
    </div>

    <div>
        <label for="id_cpf">CPF:</label>
        <input type="text" id="id_cpf" name="cpf" value="{{ form.cpf.value|default_if_none:'' }}" maxlength="11"
            required>
        {% if form.cpf.errors %}
        <div class="error">{{ form.cpf.errors }}</div>
        {% endif %}
    </div>

    <button type="submit">Salvar</button>
</form>
<a href="{% url 'listar_clientes' %}">Voltar</a>

##o arquivo de deletar o cliente
<h1>Deletar Cliente</h1>
<p>Tem certeza que deseja deletar {{ cliente.nome }}?</p>
<form method="post">
    {% csrf_token %}
    <button type="submit">Deletar</button>
</form>
<a href="{% url 'listar_clientes' %}">Voltar</a>