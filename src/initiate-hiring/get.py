import boto3
import json
import os
import uuid

dynamodb = boto3.resource('dynamodb')
table_name=os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def get_item(event, context):

    # fetch todo from the database
    result = table.get_item(
        Key={
            'job_id': event['pathParameters']['job_id']
        }
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'])
                          
    }

    return response