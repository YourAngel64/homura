from django.urls import path
from . import views

urlpatterns = [
    path('/get/', views.getUser),
    path('/post/', views.postUser),
]
