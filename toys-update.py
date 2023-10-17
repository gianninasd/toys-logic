import boto3

from dg.ToyValidator import ToyValidator


# Validates and updates the data for a toy entity
def update_toy(event, context):
  try:
    row_id = event['id']
    print('Updating toy {} for {}'.format(row_id, context.aws_request_id))

    val = ToyValidator()
    errors = val.validate(event)
    num_of_errors = len(errors)

    print('Updating toy {} - error count {}'.format(row_id, num_of_errors))

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
      dynamodb = boto3.resource('dynamodb')
      toys = dynamodb.Table('toys2')
      resp = toys.update_item(
        Key={'id': row_id},
        UpdateExpression="set #f1 = :l, model = :m, #f2 = :n, theme = :t, pieces = :p, purchaseYear = :y",
        ExpressionAttributeNames={
          '#f1': 'location',
          '#f2': 'name'
        },
        ExpressionAttributeValues={
          ':l': event['location'],
          ':m': event['model'],
          ':n': event['name'],
          ':t': event['theme'],
          ':p': event['pieces'],
          ':y': event['purchaseYear']
        },
        ReturnValues="UPDATED_NEW"
      )

      print('Updating toy {} - {}'.format(row_id, resp))

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
