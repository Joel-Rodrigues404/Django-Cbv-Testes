from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.IntegerField(blank=True, null=True)
    cpf = models.CharField()
    numero_da_conta = models.IntegerField()
    agencia = models.IntegerField()
    senha = models.CharField(max_length=8)
    email = models.EmailField(blank=True, null=True, verbose_name=("email"), max_length=254)
    senha_email = models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.nome
