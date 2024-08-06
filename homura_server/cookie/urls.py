from django.urls import path
from . import views

urlpatterns = [
    path('/post/<str:cookie_name>', views.createCookie),
    path('/get/<str:cookie_name>', views.getCookie),
    path('/delete/<str:cookie_name>', views.deleteCookie),
]
