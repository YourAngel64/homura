from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse

# Forms:
from . import forms

# Models:
from .models import UserModel


@api_view(['POST', 'GET'])
def getUser(request):
    username = ''

    # POST = Login
    # GET = cookie is available
    if request.method == 'POST':
        login_form = forms.UserLoginForm(request.POST)
        if login_form.is_valid():
            try:
                login_email = login_form.cleaned_data['email']
                login_password = login_form.cleaned_data['password']

                user = UserModel.objects.filter(
                    email=login_email, password=login_password).get()

                username = user.username
                return Response({'username': username})
            except:
                username = 'null'
    elif request.method == 'GET':
        username = request.COOKIES.get('username')
        try:
            user = UserModel.objects.filter(username=username).get()

            context = {
                'username': user.username,
                'pfp': user.pfp or 'null'
            }

            return Response(context)
        except:
            print('no se pudo')
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


@api_view(['POST'])
def createCookie(request):
    username = request.POST.get('username')
    response = HttpResponse()

    if 'username' not in request.COOKIES or username != request.COOKIES.get('username'):
        response.set_cookie('username', username, max_age=1*24*60*60)

    return response


@api_view(['GET'])
def getCookie(request):
    username = ''
    if 'username' in request.COOKIES:
        username = request.COOKIES.get('username')
    else:
        username = 'null'

    return Response({'username': username})
