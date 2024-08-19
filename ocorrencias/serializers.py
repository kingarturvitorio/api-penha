from rest_framework import serializers
from ocorrencias.models import Ocorrencia

class OcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = '__all__'