from django.urls import path, re_path
from . import consumers 

websocket_urlpatterns = [
    # re_path(r'ws/get/(?P<chat_id>\w+)/$', consumers.MessageRoom.as_asgi()),
    path('ws/get/<str:chat_id>/<str:username>/', consumers.MessageRoom.as_asgi())
]