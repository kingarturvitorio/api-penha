from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('contas/', UserListCreateView.as_view(), name='contas-list-create'),
    path('contas/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='contas-detail'),
]