from django.urls import path

from . import views

urlpatterns = [
    path('ocorrencias/', views.OcorrenciaCreateListView.as_view(), name='ocorrencia-create-list'),
    path('ocorrencias/<int:pk>/', views.OcorrenciaRetriveUpdateDestroyView.as_view(), name='ocorrencia-detail-view'),
]