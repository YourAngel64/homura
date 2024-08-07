import pymongo
import os
from dotenv import load_dotenv
load_dotenv('env_variables.env')

# Create Table - one table for Chat (everytime a chat is crated a table for it
# is created. WITH UNIQUE ID)
#
# Get Messages
# Post Messages
# Delete Messages
# Update Messages

mongodb_url = os.environ.get('mongo_db')


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


def deleteMessages(collection):
    mongo_client, mongo_db, mongo_collection = mongoConnect(collection)

    # TODO

    mongoDisconnect(mongo_client)


def updateMessages(collection):
    mongo_client, mongo_db, mongo_collection = mongoConnect(collection)

    # TODO

    mongoDisconnect(mongo_client)
