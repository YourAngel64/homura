from django.db import models


class UserModel(models.Model):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=15, unique=True)
    pfp = models.ImageField(null=True)
    about_me = models.CharField(max_length=255, null=True)
