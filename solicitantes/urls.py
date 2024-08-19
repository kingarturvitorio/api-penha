from django.urls import path

from . import views

urlpatterns = [
    path('solicitantes/', views.SolicitanteCreateListView.as_view(), name='ocorrencia-create-list'),
    path('solicitantes/<int:pk>/', views.SolicitanteRetriveUpdateDestroyView.as_view(), name='ocorrencia-detail-view'),
]