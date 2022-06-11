#!/usr/bin/env python
# coding: utf-8

import requests
import json
import base64
import os

# def hello_http(request):
def send_slack(event, context):

    ### Pub/Sub からのデータ
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')

    ### Slack 投稿データ
    slack_post_data = {}
    slack_post_data['username'] = 'handson-gcp-python-slack'
    slack_post_data['icon_emoji'] = ':ghost:'
    slack_post_data['link_names'] = '0'
    slack_post_data['text'] = pubsub_message

    ### 環境変数から Slack の Incoming Webhook の Webhook URL を読み込む
    slack_webhook_url = os.getenv('_SLACK_WEBHOOK_URL', None)

    ### Slack
    requests.post(slack_webhook_url, data = json.dumps(slack_post_data))
