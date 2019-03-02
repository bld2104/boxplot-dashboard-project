import sys

sys.path.append('packages')

import json

def handler(event, context):
  return {
    "statusCode": 200,
    "body": json.dumps("It is over!")
  }
