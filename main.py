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
    
