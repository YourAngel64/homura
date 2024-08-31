#libraries
import json
import time
from channels.generic.websocket import WebsocketConsumer
#from channels.layers import  get_channel_layer
from asgiref.sync import async_to_sync
# from asgiref.sync import sync_to_async

from .mongodb import mongoWS, closeMongoWS 

class MessageRoom(WebsocketConsumer):
    def connect(self):
        #chat_id to send to mongows connection and get correct chat
        self.chat_id = self.scope['url_route']['kwargs']['chat_id'] 
        self.username = self.scope['url_route']['kwargs']['username']
        self.chat_group_id = f'chat_{self.username}'
        
        async_to_sync(self.channel_layer.group_add)(
            self.chat_group_id,
            self.channel_name
        )

        self.accept()

        #start mongoWS connection with mongo db and getting neccesarries variables to disconect
        try:
            self.change_stream, self.mongo_client, self.thread = mongoWS(self.chat_id, self.chat_group_id)
        except Exception as ex:
            print(f'exeption for starting thread: {ex}')

        print("ws connected")
    
    def disconnect(self, code):

        async_to_sync(self.channel_layer.group_discard)(
           self.chat_group_id, 
           self.channel_name
        )

        #disconnect mongows connection
        closeMongoWS(self.change_stream, self.mongo_client, self.thread)
        print(f"ws disconnected. code: {code}")

    def receive(self, text_data):
        print(f'here ur fck message: {text_data}')

        # async_to_sync(self.channel_layer.group_send)(
        #     self.chat_group_id,
        #     {
        #         "type": "mongo.event",
        #         "message": "recieving"
        #     }
        # )
    def recieve_message(self, event):
        message = event['message']
        username = event['username']
        print(f'message: {message} by: {username}')
        self.send(text_data=json.dumps({'username': username, "message": message}))