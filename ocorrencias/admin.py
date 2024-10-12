from django.contrib import admin
from ocorrencias.models import Ocorrencia
# Register your models here.

@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'solicitante', 'nivelocorrencia','datahora', 'latocorr',
                    'longocorr','status', 'opcao_ocorrencia',)
    