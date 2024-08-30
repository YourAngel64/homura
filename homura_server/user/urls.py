from django.urls import path
from . import views

urlpatterns = [
    path('/message', views.prueba),
    path('/get/', views.getUser),
    path('/post/', views.postUser),
    path('/post/cookie', views.createCookie),
    path('/get/cookie', views.getCookie),
]
