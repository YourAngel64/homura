from rest_framework.decorators import api_view
from rest_framework.response import Response

# Forms:
from . import forms

# Models:
from .models import UserModel


@api_view(['POST'])
def getUser(request):

    username = ''

    if request.method == 'POST':
        login_form = forms.UserLoginForm(request.POST)
        if login_form.is_valid():
            try:
                login_email = login_form.cleaned_data['email']
                login_password = login_form.cleaned_data['password']

                user = UserModel.objects.filter(
                    email=login_email, password=login_password).get()

                username = user.username
            except:
                username = 'null'

    return Response({'username': username})


@api_view(['POST'])
def postUser(request):
    username = ''

    if request.method == 'POST':
        sign_form = forms.UserSignForm(request.POST)

        if sign_form.is_valid():
            try:
                sign_email = sign_form.cleaned_data['email']
                sign_password = sign_form.cleaned_data['password']
                sign_username = sign_form.cleaned_data['username']

                user = UserModel(
                    email=sign_email,
                    password=sign_password,
                    username=sign_username
                )

                user.save()

                username = sign_username
            except:
                print('sorry something wrong with creating User :(')
                username = 'null'

    return Response({'username': username})
