from django.db import models

# Create your models here.
class Produto(models.Model):
    codigoProduto = models.CharField(max_length=50)
    produto = models.CharField(max_length=50)
    valor = models.FloatField()
    validade = models.DateField()
    quantidade = models.IntegerField()