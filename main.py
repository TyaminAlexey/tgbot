import flask
from telebot import types
from config import *
from bot_handlers import bot
import os
 
server = flask.Flask(__name__)
 
 
import json
import requests
i = 1
def handler(event, context):
    body = json.loads(event['body'])
    global i
    i += 2
    return {
        
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            
            'text': i                       
            
        }),
        'isBase64Encoded': False
    }
 
 
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
