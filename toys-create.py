import boto3
import uuid

from dg.ToyValidator import ToyValidator


# Validates and create the data for a toy entity
def create_toy(event, context):
  try:
    print('Creating toy for {}'.format(context.aws_request_id))

    val = ToyValidator()
    errors = val.validate(event)
    num_of_errors = len(errors)

    print('Creating toy - error count {}'.format(num_of_errors))

    if num_of_errors > 0:
      resp_json = {
        "statusCode": 400,
        "headers": {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*"
        },
        "body": errors
      }
      return resp_json
    else:
      row_id = str(uuid.uuid4())
      dynamodb = boto3.resource('dynamodb')
      toys = dynamodb.Table('toys2')
      resp = toys.put_item(
        Item={
          'id': row_id,
          'location': event['location'],
          'model': event['model'],
          'name': event['name'],
          'theme': event['theme'],
          'pieces': event['pieces'],
          'purchaseYear': event['purchaseYear']
        }
      )

      print('Creating toy {} - {}'.format(row_id, resp))

      return {
        "statusCode": 200,
        "headers": {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*"
        },
        "body": resp
      }
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
