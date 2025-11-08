"""
ASGI config for LinkaProj project.

It exposes the ASGI callable as a module-level variable named ``application``.
For more information, see:
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack  #  important for user sessions
from ChatApp import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LinkaProj.settings')

django.setup()

# Create Django ASGI application
django_asgi_app = get_asgi_application()

#  Combine HTTP and WebSocket
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(  # allows authentication/session data in websockets
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})
