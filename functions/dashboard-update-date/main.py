import sys

sys.path.append('packages')

import requests
import json

def handler(event, context):
  statusCode = 204
  body = ""

  if event["queryStringParameters"] and event["queryStringParameters"]["script"]:
    try:
      response = requests.get(event["queryStringParameters"]["script"], allow_redirects=True)

      exec(response.content)
    except Exception as e:
      print("ERROR:" + str(e))

      statusCode = 500
      body = {"error": str(e)}
  else:
    statusCode = 400
    body = {"error": "Script parameter can't be empty"}


  return {
    "statusCode": statusCode,
    "headers": {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET"
    },
    "body": json.dumps(body)
  }