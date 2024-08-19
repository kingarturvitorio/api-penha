from rest_framework import serializers
from solicitantes.models import Solicitante

class SolicitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitante
        fields = '__all__'