from django import forms
from django.contrib.postgres.fields import ArrayField


class CreateChat(forms.Form):
    chat_name = forms.CharField(max_length=255),
    users = ArrayField(forms.CharField(max_length=255)),
    users_admin = ArrayField(forms.CharField(max_length=255)),
