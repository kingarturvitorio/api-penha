from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('contas.urls')),
    path('api/v1/', include('solicitantes.urls')),
    path('api/v1/', include('ocorrencias.urls')),
    path('api/v1/', include('gps_websocket.urls')),
    
]
