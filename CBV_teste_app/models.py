from django.db import models

# Create your models here.


class Produtos(models.Model):
    
    nome = models.CharField(max_length=50)
    preço = models.FloatField()

    def __str__(self) -> str:
        return self.nome