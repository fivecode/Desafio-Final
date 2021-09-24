from django.db import models
from django.db.models.query import prefetch_related_objects

class Empresa(models.Model):
    cnpj = models.CharField(max_length=150)
    nomeDaEmpresa = models.CharField(max_length=250)
    email = models.CharField(max_length=100)
    telefone = models.IntegerField()

class Produto(models.Model):
    nome =
    descricao = 
    preco =
    estoque =
    id.Empresa     

#class Proprietaria(models.Model):
#nome = models.CharField(max_length=100)
#rg = models.IntegerField()
#idCarro = models.ForeignKey(Carros, models.DO_NOTHING, db_column='id', blank=True, null=True)
   