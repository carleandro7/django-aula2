from django.db import models

# Create your models here.
class Cliente(models.Model):
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
