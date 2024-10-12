from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import ContasPolicialSerializer
from .models import ContaPolicial
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer

class ContaPolicialCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ContaPolicial.objects.all()
    serializer_class = ContasPolicialSerializer

class ContaPolicialRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ContaPolicial.objects.all()
    serializer_class = ContasPolicialSerializer

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        # Passa os dados do request para o LoginSerializer
        serializer = LoginSerializer(data=request.data)

        # Valida o serializer
        if serializer.is_valid():
            # Pega o policial autenticado a partir dos dados validados
            policial = serializer.validated_data['user']
            
            # Gera o token de refresh e access para o policial autenticado
            refresh = RefreshToken.for_user(policial)

            # Retorna os tokens JWT como resposta
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            # Se houver erro de validação, retorna o erro
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)