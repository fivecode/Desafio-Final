from django.db import models
from django.db.models.query import prefetch_related_objects

class Empresa(models.Model):
    cnpj = models.CharField(max_length=150)
    nomeDaEmpresa = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    telefone = models.IntegerField()

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=20, decimal_places=2)
    estoque = models.IntegerField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True)
    
