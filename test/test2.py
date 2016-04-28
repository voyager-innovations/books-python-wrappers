#!/usr/local/bin/python3

from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id="anything",
                          aws_secret_access_key="anything",
                          region_name="us-west-2",
                          endpoint_url="http://localhost:8000")


table = dynamodb.Table('Contacts')

try:
    response = table.query(
        IndexName='ContactDateIndex',
        KeyConditionExpression=Key('date_modified').eq('2016-03-27')
    )
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    item = response['Items']
    print(json.dumps(item))