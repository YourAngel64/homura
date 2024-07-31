from rest_framework.decorators import api_view
from rest_framework.response import Response

# Forms
from . import forms

# Models
from . import models


@api_view(['POST'])
def postChat(request):
    if request.method == 'POST':
        try:
            print(request.POST)
            chat_form = forms.CreateChat(request.POST)

            if chat_form.is_valid():

                print(chat_form.clean())
                chat_name = chat_form.cleaned_data['chat_name']
                users = chat_form.cleaned_data['users']
                users_admin = chat_form.cleaned_data['users_admin']
                description = chat_form.cleaned_data['description']
                unique_id = chat_form.cleaned_data['unique_id']

                chat_model = models.Chat(
                    chat_name=chat_name,
                    users=users,
                    users_admin=users_admin,
                    description=description,
                    unique_id=unique_id
                )

                chat_model.save()
                return Response({'status': 'success'})
        except Exception as er:
            print(er)
            return Response({'status': 'fail'})


@api_view(['GET'])
def getChat(request):

    if request.method == 'GET':
        try:
            username = request.COOKIES.get('username')
            chat_list = models.Chat.objects.filter(
                username=username).get('chat_name')
            return Response({'chats': chat_list})
        except:
            return Response({'chats': 'null'})
