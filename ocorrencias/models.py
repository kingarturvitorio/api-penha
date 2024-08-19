from django.db import models
from solicitantes.models import Solicitante
# Create your models here.

# Create your models here.
class Ocorrencia(models.Model):
    solicitante = models.ForeignKey(
        Solicitante, 
        on_delete=models.PROTECT,
        related_name='solicitante'
    )
    nivelocorrencia = models.IntegerField()
    datahora = models.DateField(null=True, blank=True)
    latocorr = models.FloatField()
    longocorr = models.FloatField()
    status = models.IntegerField()
    link = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.solicitante}'