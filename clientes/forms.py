from django import forms
from .models import Cliente
from .models import Pedido

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf']
    


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['descricao', 'valor', 'cliente']