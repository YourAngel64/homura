from django import forms
from django.contrib.postgres.fields import ArrayField


class CreateChat(forms.Form):
    chat_name = forms.CharField(max_length=255)
    users = ArrayField(forms.CharField(max_length=255))
    users_admin = ArrayField(forms.CharField(max_length=255))
    description = forms.CharField(max_length=255)
    unique_id = forms.CharField(max_length=255)


class CreateMessage(forms.Form):
    message = forms.CharField(max_length=500)
    user = forms.CharField(max_length=255)
    chat = forms.CharField(max_length=255)
