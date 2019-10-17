import json
import logging
import logging.config

try:
  import unzip_requirements
except ImportError:
  pass

def handler(event, context):
    """
    Incoming lambda handler
    """

    logger = logging.getLogger("handler")

    body = {
        "message": "Handler responding here",
        "input": "event"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
