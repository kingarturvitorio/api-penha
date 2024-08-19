from django.contrib import admin
from solicitantes.models import Solicitante
# Register your models here.

@admin.register(Solicitante)
class SolicitanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf',)