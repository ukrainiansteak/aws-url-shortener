import os
import json
import random
import string

import boto3

dynamodb_client = boto3.client("dynamodb")
TABLE_NAME = os.environ["TABLE_NAME"]
DNS_RECORD = os.environ["DNS_RECORD"]

def handler(event, context):

    event_body = event.get("body")
    if not event_body:
        return {
            "statusCode": 400, "body": json.dumps({
                "error": "body is empty"
            })
        }

    request_body = json.loads(event_body)
    long_url = request_body.get("long_url")
    if not long_url:
        return {
            "statusCode": 400, "body": json.dumps({
                "error": "param long_url required"
            })
        }

    url_id = "".join(random.choices(string.ascii_letters + string.digits, k=6))

    dynamodb_client.put_item(
        TableName=TABLE_NAME,
        Item={
            'url_id': {"S": url_id},
            'long_url': {"S": long_url}
        }
    )

    short_url = DNS_RECORD + "link/" + url_id

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "url_id": url_id,
                "short_url": short_url
            }
        )
    }
