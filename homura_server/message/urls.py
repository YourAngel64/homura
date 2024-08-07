from django.urls import path
from . import views

urlpatterns = [
    path("/chat/get", views.getChat),
    path("/chat/post", views.postChat),
    path("/chat/get/<str:chat_id>", views.getChatInfo),
    path("/get/<str:chat_id>", views.getMessages),
    path("/post/<str:chat_id>", views.postMessages),
]
