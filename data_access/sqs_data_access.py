import boto3
import json

sqs = boto3.client('sqs')
queue_url = 'https://queue.amazonaws.com/856841379672/TrackDelayQueue'

def sendMessage(message):
    sqs.send_message(
        QueueUrl = queue_url,
        DelaySeconds = 10,
        MessageAttributes={
            'alert_id': {
                'DataType': 'String',
                'StringValue': str(record_dict["alert_id"])
                }
        },
        MessageBody=json.dumps(message)
    )