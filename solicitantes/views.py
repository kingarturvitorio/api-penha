from rest_framework import generics
from solicitantes.models import Solicitante
from solicitantes.serializers import SolicitanteSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class SolicitanteCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Solicitante.objects.all()
    serializer_class = SolicitanteSerializer

class SolicitanteRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Solicitante.objects.all()
    serializer_class = SolicitanteSerializer