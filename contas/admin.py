from django.contrib import admin
from contas.models import ContaPolicial
# Register your models here.

@admin.register(ContaPolicial)
class ContaPolicialAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'nregistro',)