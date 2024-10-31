from django.db import models
from solicitantes.models import Solicitante
# Create your models here.

OPCOES_OCORRENCIA = [
        ("ATENDIDA","Atendida"),
        ("EM ATENDIMENTO","Em atendimento"),
        ("CONCLUIDA","Concluida"),
        ("EM AVALIACAO","Em avaliacao"),
    ]
        
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
    opcao_ocorrencia = models.CharField(max_length=100, choices=OPCOES_OCORRENCIA, default='', null=True, blank=True)
    
    def __str__(self):
        return f'{self.solicitante}'