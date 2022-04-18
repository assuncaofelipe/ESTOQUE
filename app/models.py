from asyncio.windows_events import NULL
from django.db import models

# Create your models here.
class Produto(models.Model):
    codigoProduto = models.CharField(max_length=30, default=None, unique=True)
    produto = models.CharField(max_length=50)
    valor = models.FloatField()
    validade = models.DateField(blank=True, null=True)
    quantidade = models.IntegerField()