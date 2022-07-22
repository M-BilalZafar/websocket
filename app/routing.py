from django.urls import path,re_path
from . import consumers

websocket_urlpatterns = [
    
    path(r'ws/sc/', consumers.MySyncConsumer.as_asgi()),
    
    
]