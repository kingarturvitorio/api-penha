from rest_framework import serializers
from ocorrencias.models import Ocorrencia
from django.contrib.auth import authenticate

class OcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user is None:
            raise serializers.ValidationError('Invalid Credentials')
        attrs['user'] = user
        return attrs