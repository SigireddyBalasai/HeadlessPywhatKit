#imports for using sqs 
import boto3
import json
import os
from HeadlessPywhatKit.whats import WhatsApp

wa = WhatsApp()

#read credentials from keys.json
with open('keys.json') as f:
    data = json.load(f)
    access_key = data['access_key']
    secret_key = data['secret_key']
    region = data['region']
    queurl = data['queurl'] 
#initialize boto3 client
sqs = boto3.client('sqs', aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region)


#read messages from queue
def read_and_process_message(message_processor):
    response = sqs.receive_message(
        QueueUrl=queurl,
        MaxNumberOfMessages=1,
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )
    message = response['Messages'][0]
    receipt_handle = message['ReceiptHandle']
    message_processor(message)
    # Delete received message from queue
    sqs.delete_message(
        QueueUrl=queurl,
        ReceiptHandle=receipt_handle
    )
    return message

#process message
def process_message(message):
    print(message)
    body = message['Body']
    body = json.loads(body)
    print(body)
    phone = body['phone']
    message = body['message']
    wa.send_user_message(phone, message)

#send message to queue
def send_message(phone, message):
    message = {
        'phone': phone,
        'message': message
    }
    message = json.dumps(message)
    response = sqs.send_message(
        QueueUrl=queurl,
        MessageBody=(
            message
        )
    )
    print(response['MessageId'])

send_message("+923015412877", "Hello World")

while True:
    try:
        read_and_process_message(process_message)
    except:
        pass