from rest_framework import generics
from solicitantes.models import Solicitante
from solicitantes.serializers import SolicitanteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer
# Create your views here.

class SolicitanteCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Solicitante.objects.all()
    serializer_class = SolicitanteSerializer

class SolicitanteRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Solicitante.objects.all()
    serializer_class = SolicitanteSerializer

class LoginViewSolicitante(APIView):
    """
    View para login de Solicitante usando CPF e Senha.
    """
    def post(self, request, *args, **kwargs):
        # Passa os dados do request para o LoginSerializer
        serializer = LoginSerializer(data=request.data)

        # Valida o serializer
        if serializer.is_valid():
            # Pega o solicitante autenticado a partir dos dados validados do serializer
            solicitante = serializer.validated_data['user']

            # Gera o token de refresh e access para o solicitante autenticado
            refresh = RefreshToken.for_user(solicitante)

            # Retorna os tokens JWT e o ID do usuário como resposta
            return Response({
                'id': solicitante.id,  # Adiciona o ID do solicitante na resposta
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            # Se houver erro de validação, retorna o erro
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    