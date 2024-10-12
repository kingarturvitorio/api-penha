from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from .models import ContaPolicial

class ContasPolicialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContaPolicial
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    nregistro = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        nregistro = attrs.get('nregistro')
        password = attrs.get('password')

        # Tenta buscar o policial pelo número de registro (nregistro)
        try:
            policial = ContaPolicial.objects.get(nregistro=nregistro)
        except ContaPolicial.DoesNotExist:
            raise serializers.ValidationError('Registro não encontrado.')

        # Verifica a senha
        if not check_password(password, policial.password):
            raise serializers.ValidationError('Credenciais inválidas.')

        # Caso a autenticação seja bem-sucedida, retornamos o policial
        attrs['user'] = policial
        return attrs