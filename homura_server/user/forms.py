from django import forms


class UserLoginForm(forms.Form):
    email = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)


class UserSignForm(forms.Form):
    email = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    username = forms.CharField(max_length=255)
