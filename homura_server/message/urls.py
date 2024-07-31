from django.urls import path
from . import views

urlpatterns = [
    path("/chat/get", views.getChat),
    path("/chat/post", views.postChat),
]
