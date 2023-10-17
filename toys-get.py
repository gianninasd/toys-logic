import os
import json
import boto3
import decimal


# internal class used to convert decimal values to a string
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)


# A Lambda function handler that processes the test payload
def lambda_handler(event, context):
    awsregion = os.environ['AWS_REGION']
    print('toys-get received event, invoked by {} on {}'.format(context.invoked_function_arn, awsregion))

    try:
        dynamodb = boto3.resource('dynamodb')
        toys = dynamodb.Table('toys2')
        data = toys.scan()
        items = data['Items']
        print('all rows: {}'.format(items))

        resp_json = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": items
        }

        return json.dumps(resp_json, cls=DecimalEncoder)
    except Exception as err:
        print('Unknown error occurred: {}'.format(err))

        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": {
                "error": "Unknown error occurred"
            }
        }
