import pymongo
import os
from dotenv import load_dotenv
load_dotenv('env_variables.env')

#libraries for WS
import threading
import json
import time
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Create Table - one table for Chat (everytime a chat is crated a table for it
# is created. WITH UNIQUE ID)
#
# Get Messages
# Post Messages
# Delete Messages
# Update Messages

mongodb_url = os.environ.get('mongo_db')


class mongoWS_thread(threading.Thread):
    def __init__(self, change_stream, channel_layer, chat_group_id):
        super().__init__()
        #self.chat_id = chat_id
        #self.chat_group_id = chat_group_id

        self.change_stream = change_stream
        self.channel_layer = channel_layer
        self.chat_group_id = chat_group_id

        self.__stop_event = threading.Event()
        time.sleep(1)
        print('ola')
    
    def run(self):
        while not self.__stop_event.is_set():
            for change in self.change_stream:
                if change['operationType'] == 'insert':
                    print(f'change: {change}')
                    new_message = change['fullDocument']
                    print(new_message['message'])
                    # async_to_sync(self.channel_layer.group_send)(
                    #     self.chat_group_id,
                    #     {
                    #         'type': 'mongo.event',
                    #         'message': f'new message: {json.dumps(new_message)}'
                    #     } 
                    # )
                #self.mongo_client = mongoWS(self.chat_id, self.chat_group_id)

    def stop(self):
        time.sleep(1)
        self.__stop_event.set()
        #closeMongoWS(self.mongo_client)


def mongoConnect(collection):
    mongo_client = pymongo.MongoClient(mongodb_url)
    mongo_db = mongo_client['homura-messages']
    mongo_collection = mongo_db[collection]

    return mongo_client, mongo_db, mongo_collection


def mongoDisconnect(mongo_client):
    mongo_client.close()


def getMessages(collection):
    mongo_client, mongo_db, mongo_collection = mongoConnect(collection)

    messages = mongo_collection.find()

    message_array = []
    for message in messages:
        message_array.append(message)

    mongoDisconnect(mongo_client)
    return message_array


def postMessages(collection, message, username):
    mongo_client, mongo_db, mongo_collection = mongoConnect(collection)

    try:
        mongo_collection.insert_one({
            'username': username,
            'message': message
        })
        mongoDisconnect(mongo_client)
        return {'staus': 'message posted!'}
    except Exception as ex:
        print(ex)
        mongoDisconnect(mongo_client)
        return {'status': 'failed'}

def mongoWS(chat_id, chat_group_id):
    try:

        mongo_client, mongo_db, mongo_collection = mongoConnect(chat_id)
        change_stream = mongo_collection.watch() 
        channel_layer = get_channel_layer()
         
        thread = mongoWS_thread(change_stream=change_stream, channel_layer=channel_layer, chat_group_id=chat_group_id)
        thread.start()

    except Exception as ex:
        print(f'here exeption: {ex}')
    finally:
        return change_stream, mongo_client, thread
    # thread = threading.Thread(target=function)
    # thread.start()


def closeMongoWS(change_stream, mongo_client, thread):
    try:
        if change_stream.alive:
            print('clossing...')
            thread.stop()
            change_stream.close()
            mongo_client.close()
            print('closed :D')
    except Exception as ex:
        print(f"here exeption for closing: {ex}")
    finally:
        print('everything fine in closing')


def deleteMessages(collection):
    mongo_client, mongo_db, mongo_collection = mongoConnect(collection)

    # TODO

    mongoDisconnect(mongo_client)


def updateMessages(collection):
    mongo_client, mongo_db, mongo_collection = mongoConnect(collection)

    # TODO

    mongoDisconnect(mongo_client)
