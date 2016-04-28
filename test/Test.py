import boto3
import json
import decimal
from boto3 import dynamodb
from boto3.session import Session

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb_session = Session(aws_access_key_id='AKIAJQGBWRX6PSWB4KHQ',
              aws_secret_access_key='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',
              region_name='us-west-2')

dynamodb = dynamodb_session.resource('dynamodb')

table_contacts = dynamodb.Table('Contacts')

company_name = "ABC"
email = 'abc@email.com'


# response = table.get_item(
#     Key={
#         'Company Name': company_name,
#         'Email': email
#     }
# )
#print(response['Item'])

#scan - retrieved all items
response = table_contacts.scan()
for i in response['Items']:
    print(json.dumps(i, cls=DecimalEncoder))


table_accounts = dynamodb.Table('Accounts')
response = table_accounts.scan()
for i in response['Items']:
    print(json.dumps(i, cls=DecimalEncoder))

table_opportunitues = dynamodb.Table('Opportunities')
response = table_opportunitues.scan()
for i in response['Items']:
    print(json.dumps(i, cls=DecimalEncoder))
