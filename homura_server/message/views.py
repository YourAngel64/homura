from threading import ExceptHookArgs
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Forms
from . import forms

# Models
from . import models


@api_view(['POST'])
def postChat(request):
    if request.method == 'POST':
        chat = forms.CreateChat(request.POST)
        if chat.is_valid():
            try:
                # users and users_admin are arrays therefore they get special treatment :3
                chat_name = chat.cleaned_data['chat_name']
                users = request.POST.getlist('users[]')
                users_admin = request.POST.getlist('users_admin[]')
                description = chat.cleaned_data['description']
                unique_id = chat.cleaned_data['unique_id']

                chat_model = models.Chat(
                    chat_name=chat_name,
                    users=users,
                    users_admin=users_admin,
                    description=description,
                    unique_id=unique_id
                )

                chat_model.save()
                return Response({'status': 'success'})
            except Exception as err:
                print(err)
                return Response({'status': 'fail'})

    return Response({'status': 'aqui'})


@api_view(['GET'])
def getChat(request):

    if request.method == 'GET':
        try:
            username = request.COOKIES.get('username')
            chat_list = models.Chat.objects.filter(
                users__contains=[username]).all().values()

            chat_array = []
            for chat in chat_list:
                chat_array.append(chat.get('unique_id'))

            return Response(chat_array)
        except Exception as err:
            print(err)
            return Response([])
