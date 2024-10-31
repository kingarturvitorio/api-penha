
from django.core.asgi import get_asgi_application

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
from gps_websocket import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apiMariaPenha.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns
        )
    )),
})
