from django.urls import path
from . import views


urlpatterns = [
    path('hello-world/', views.hello_world),
    path('prueba/', views.prueba),
    path('prueba/post/', views.post_test)
]
