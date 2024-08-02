from django.db import models
from django.contrib.postgres.fields import ArrayField


class Chat(models.Model):
    chat_name = models.CharField(max_length=255, default='')
    users = ArrayField(models.CharField(max_length=255), default=[''])
    users_admin = ArrayField(models.CharField(max_length=255), default=[''])
    pfp = models.ImageField(null=True)
    description = models.CharField(max_length=255, null=True, default='')
    unique_id = models.CharField(max_length=255, unique=True, default='')
