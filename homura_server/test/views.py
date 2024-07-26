from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.middleware import csrf
from .forms import PostForm


@api_view(['GET'])
def hello_world(request):
    return Response({
        'message': 'hello django :3',
        'csrf_token': csrf.get_token(request),
    })


@api_view(['GET'])
def prueba(request):
    context = {
        'username': "Enten",
        'message': 'ola'
    }

    return Response(context)


@api_view(['POST'])
def post_test(request):
    context = {
        'username': 'null',
        'message': 'null'
    }

    myform = PostForm(request.POST)
    if myform.is_valid():
        username = myform.cleaned_data['username']
        message = myform.cleaned_data['message']
        context = {
            'username': username,
            'message': message
        }

    return Response(context)
