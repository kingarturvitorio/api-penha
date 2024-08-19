from django.db import models


# Create your models here.
class Solicitante(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=14)
    tplogradouro = models.CharField(max_length=100)
    nres = models.CharField(max_length=10)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)
    dtnasc = models.DateField(null=True, blank=True)
    dtcadastro = models.DateField(null=True, blank=True)
    processo = models.CharField(max_length=30)
    latres = models.FloatField()
    longres = models.FloatField()
    observacoes = models.CharField(max_length=30)
    status = models.IntegerField()
    
    def __str__(self):
        return self.nome
