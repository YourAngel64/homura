from django import forms


class PostForm(forms.Form):
    username = forms.CharField(max_length=255)
    message = forms.CharField(max_length=255)
