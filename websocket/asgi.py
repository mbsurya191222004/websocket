import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import ws.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websocket.settings")
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Django views
    "websocket": AuthMiddlewareStack(
        URLRouter(
            ws.routing.websocket_urlpatterns
        )
    ),
})
