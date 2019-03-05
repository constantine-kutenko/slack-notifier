# slack-notifier

## Overview

A package that provides functionality for sending simple messages to a particular Slack channel.

## Dependencies

- Python 3.x
- Python libraries:
    - requests
    - json
    - sys

## Installation

The package can be installed from a repository

```bash
    pip install slacknotifier
```

## Usage

### Send a message

To send a message to a Slack channel use the channel's ID:

```python
    import slacknotifier
    
    # Define values for payload
    username = "Slack notifier"
    channel = "updatenotifications"
    caption = "Message caption"
    title = "Message title"
    pretext = "Attachement message body"
    text = "Message body"
    color = "OK"
    mrkdwn = "True"
    webhook_url = 'https://hooks.slack.com/services/XXXXXXXX/XXXXXXXXXX/XXXXXXXXXXXXXXXXXXXXXXXXX'

    # A simple example of payload structure
    payload = {
        "username": "%s" % username,
        "text": "%s" % caption,
        "channel": "%s" % channel,
        "attachments": [
            {
                "title": "%s" % title,
                "pretext": "%s" % pretext,
                "text": "%s" % text,
                "color": "%s" % color,
                "mrkdwn_in": ['text']
            }
        ]
    }
    
    # Send
    slacknotifier.send(payload, webhook_url)
```

### Build the package

Build artifacts for the package:

```bash
python setup.py check sdist bdist
```

### Upload the package

Manual upload artifacts into a repository keeping in mind that you have properly prepared ~/.pypirc file:

```bash
twine upload -r <repo_name> dist/slacknotifier-<verion>.tar.gz
```
