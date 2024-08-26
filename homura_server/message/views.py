from rest_framework.decorators import api_view
from rest_framework.response import Response

# Forms
from . import forms

# Models
from . import models
from user.models import UserModel

# MongoDB
from . import mongodb


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

    return Response({'status': 'null'})


@api_view(['GET'])
def getChat(request):

    if request.method == 'GET':
        try:
            username = request.COOKIES.get('username')
            chat_list = models.Chat.objects.filter(
                users__contains=[username]).all().values()

            chat_dictionary_array = []
            i = 0
            for chat in chat_list:
                chat_dictionary_array.append({
                    'id': i,
                    'chat_name': chat.get('chat_name'),
                    'description': chat.get('description'),
                    'unique_id': chat.get('unique_id')
                })
                i += 1

            return Response(chat_dictionary_array)
        except Exception as err:
            print(err)
            return Response([])


@api_view(['GET'])
def getChatInfo(request, chat_id):
    try:
        chat = models.Chat.objects.filter(unique_id=chat_id).get()
        info = {
            'chat_name': chat.chat_name
        }

        return Response(info)

    except Exception as ex:
        print(ex)
        return Response({})


@api_view(['POST'])
def addUser(request, chat_id):
    add_user = request.POST.get('add_user')

    # Check if user in data base
    try:
        user = UserModel.objects.filter(username=add_user).get()
        chat = models.Chat.objects.filter(unique_id=chat_id).get()

        if user.username not in chat.users:
            chat.users.append(user.username)

        chat.save()

        return Response({'user': user.username})
    except Exception as ex:
        print(ex)
        return Response({'user': 'null'})


@api_view(['GET'])
def getMessages(request, chat_id):
    try:
        messages = mongodb.getMessages(chat_id)

        message_array = []
        for message in messages:
            message_dic = {
                'username': message['username'],
                'message': message['message']
            }

            message_array.append(message_dic)

        data = {
            'status': 'ola',
            'messages': message_array
        }
        return Response(data)

    except Exception as err:
        print(f"this is it: {err}")

    return Response({"status": "kys"})


@ api_view(['POST'])
def postMessages(request, chat_id):
    if request.method == 'POST':
        message_form = forms.CreateMessage(request.POST)
        if message_form.is_valid():
            try:
                message = message_form.cleaned_data['message']
                username = message_form.cleaned_data['username']

                status = mongodb.postMessages(chat_id, message, username)
                return Response(status)

            except Exception as err:
                print(err)
                return Response({'status': 'failed'})
