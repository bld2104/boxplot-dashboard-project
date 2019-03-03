import sys

sys.path.append('packages')

import requests
import json

def handler(event, context):
  script_path = "https://s3.amazonaws.com/homerise-dev/development/uploads/project/photos/92/initial_data_retrieval_twitter.py"

  response = requests.get(script_path, allow_redirects=True)

  # if status_code == 200
  exec(response.content)
  # else
    # print("error !!")

  return {
    "statusCode": 200,
    "body": json.dumps("It is over! Or Error")
  }
