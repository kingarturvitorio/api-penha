from rest_framework import serializers
from solicitantes.models import Solicitante
from django.contrib.auth.hashers import check_password

class SolicitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitante
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    cpf = serializers.CharField(max_length=11)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        cpf = attrs.get('cpf')
        password = attrs.get('password')

        # Buscar o solicitante com base no CPF
        try:
            solicitante = Solicitante.objects.get(cpf=cpf)
        except Solicitante.DoesNotExist:
            raise serializers.ValidationError('Credenciais inválidas.')

        # Verificar se a senha é válida (considerando que as senhas estejam armazenadas com hashing)
        if not check_password(password, solicitante.password):
            raise serializers.ValidationError('Credenciais inválidas.')

        # Adicionar o solicitante autenticado ao attrs
        attrs['user'] = solicitante
        return attrs

