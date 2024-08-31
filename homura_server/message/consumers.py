#libraries
import json
from channels.generic.websocket import WebsocketConsumer
#from channels.layers import  get_channel_layer
from asgiref.sync import async_to_sync
# from asgiref.sync import sync_to_async

from .mongodb import mongoWS, closeMongoWS 
import threading

#local

# Step 1 - Update whenever client sends message DONE
# Step 2- update whenever db recieves new message



class MessageRoom(WebsocketConsumer):
    def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['chat_id'] 
        self.chat_group_id = f'chat_{self.chat_id}'
        
        async_to_sync(self.channel_layer.group_add)(
            self.chat_group_id,
            self.channel_name
        )

        self.accept()

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

        closeMongoWS(self.change_stream, self.mongo_client, self.thread)
        print(f"ws disconnected. code: {code}")

    def receive(self, text_data):
        print(f'here ur fck message: {text_data}')

        async_to_sync(self.channel_layer.group_send)(
            self.chat_group_id,
            {
                "type": "mongo.event",
                "message": "recieving"
            }
        )
    def recieve_message(self, event):
        message = event['message']
        print('eii')
        self.send(text_data=json.dumps({"message": message}))
         
    #async def send(self, text_data=None, bytes_data=None, close=False):
    #    await self.send(text_data=json.dumps({"message": "sending"}))