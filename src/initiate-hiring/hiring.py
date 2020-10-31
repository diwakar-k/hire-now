import boto3
import json
import os
import uuid

dynamodb = boto3.resource('dynamodb')
table_name=os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def post(event, context):
    try:
        req_body = json.loads(event['body'])
        req_fields= {
            'job_id': req_body['job_id'],
            'name': req_body['name'],
            'location': req_body['location'],
            'skills': req_body['skills']
        }

        table.put_item(
            Item=req_fields
        )
        resp = {
            'statusCode':200,
            "message": "Job Posted Successfully",
        }
        return json.dumps(resp)
    except Exception as e:
        response = {
            'statusCode': 500,
            'message': str(e)
        }
        raise Exception(json.dumps(response))


