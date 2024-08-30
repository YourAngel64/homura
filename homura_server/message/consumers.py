#libraries
import json
from channels.generic.websocket import WebsocketConsumer
#from channels.layers import  get_channel_layer
from asgiref.sync import async_to_sync
# from asgiref.sync import sync_to_async

#local

class MessageRoom(WebsocketConsumer):
    def connect(self):
        print('HEY')
        self.chat_id = self.scope['url_route']['kwargs']['chat_id'] 
        self.chat_group_id = f'chat_{self.chat_id}'
        
        async_to_sync(self.channel_layer.group_add)(
            self.chat_group_id,
            self.chat_id
        )

        self.accept()
        print("ws connected")
    
    def disconnect(self, code):

        async_to_sync(self.channel_layer.group_discard)(
           self.chat_group_id, 
           self.chat_id
        )
        print(f"ws disconnected. code: {code}")

    def receive(self, text_data):
        print('recieved thi shit')
        print(f'here ur fck message: {text_data}')

        async_to_sync(self.channel_layer.group_send)(
            self.chat_group_id,
            {
                "type": "chat.message",
                "message": "recieving"
            }
        )

    #async def send(self, text_data=None, bytes_data=None, close=False):
    #    await self.send(text_data=json.dumps({"message": "sending"}))