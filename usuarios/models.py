from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True, blank=False)

    # Sobrescrevemos os campos 'groups' e 'user_permissions' para removê-los
    username = None
    groups = None
    user_permissions = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'cpf', 'telefone']

    def __str__(self):
        return f'{self.nome}#{self.email}'
  