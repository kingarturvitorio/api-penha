from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Solicitante(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=14)
    logradouro = models.CharField(max_length=100)
    nres = models.CharField(max_length=10)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)
    dtnasc = models.DateField(null=True, blank=True)
    dtcadastro = models.DateField(null=True, blank=True)
    processo = models.CharField(max_length=30)
    observacoes = models.CharField(max_length=30)
    status = models.IntegerField()
    password = models.CharField(max_length=128)  # Tamanho ajustado para hash

    def save(self, *args, **kwargs):
        # Ao salvar, garanta que a senha seja armazenada como hash
        if self.password and not self.password.startswith('pbkdf2'):
            self.password = make_password(self.password)
        super(Solicitante, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.nome


