from rest_framework import generics
from ocorrencias.models import Ocorrencia
from ocorrencias.serializers import OcorrenciaSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class OcorrenciaCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer

class OcorrenciaRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer