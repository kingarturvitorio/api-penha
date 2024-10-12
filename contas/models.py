from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.
       
# Create your models here.
class ContaPolicial(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    nregistro = models.CharField(max_length=10)

    # Altere o campo 'password' para que tenha tamanho suficiente para armazenar hashes
    password = models.CharField(max_length=128)  # Tamanho ajustado para hash

    def save(self, *args, **kwargs):
        # Ao salvar, garanta que a senha seja armazenada como hash
        if self.password and not self.password.startswith('pbkdf2'):
            self.password = make_password(self.password)
        super(ContaPolicial, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.nome}'