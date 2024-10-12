from django.urls import path
from .views import ContaPolicialCreateListView, ContaPolicialRetriveUpdateDestroyView, LoginView

urlpatterns = [
    path('contas/', ContaPolicialCreateListView.as_view(), name='contas-list-create'),
    path('contas/<int:pk>/', ContaPolicialRetriveUpdateDestroyView.as_view(), name='contas-detail'),
    path('contas/login/', LoginView.as_view(), name='contas-login'),
]