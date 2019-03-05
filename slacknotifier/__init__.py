import requests
import json
import sys

slacknotifier_version = "0.1"


def version():
    """Returns a version of the package"""
    return slacknotifier_version


def send(payload, webhook_url):
    """Sends notification to Slack"""
    # Send message as a JSON string
    try:
        response = requests.post(
            webhook_url,
            data=json.dumps(payload),
            headers={'Content-Type': 'application/json'})
    except requests.exceptions.ConnectionError as err:
        print("Connection error:\n%s" % err)
        sys.exit(1)
    except requests.exceptions.Timeout as err:
        print("Timeout:\n%s" % err)
        sys.exit(1)
    except requests.exceptions.HTTPError as err:
        print("HTTP error:\n%s" % err)
        sys.exit(1)

    # Return HTTP status code and description for further analysis
    return response.status_code, response.text
