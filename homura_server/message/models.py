from django.db import models
from django.contrib.postgres.fields import ArrayField


class Chat(models.Model):
    chat_name = models.CharField(max_length=255),
    users = ArrayField(models.CharField(max_length=255), null=False),
    users_admin = ArrayField(models.CharField(max_length=255), null=False),
    pfp = models.ImageField(null=True),
    description = models.CharField(max_length=255, null=True),
    unique_id = models.CharField(max_length=15, null=False, unique=True),
