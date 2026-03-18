from flask import Flask, request, abort
import requests
import os

app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = "eh5UPbWRqIs1yKwaw8jX6T8nb6ev5Kp7voYRc058+T6AYs7fiiRgUyvRi/je8spTf1BeWUdfHJBNmbIk337IvCSLFu/i2q2BBu8y3/QCZd9VdcQlrXmxV4/HFeOluMzpXgziPlf65m3JbGrIgtlHKQdB04t89/1O/w1cDnyilFU="

@app.route("/callback", methods=['POST'])
def callback():
    body = request.json

    for event in body['events']:
        if event['type'] == 'message':
            reply_token = event['replyToken']

            # とりあえず固定返信
            reply_message(reply_token, "龍勝院ですわ。")

    return 'OK'


def reply_message(reply_token, text):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}"
    }

    data = {
        "replyToken": reply_token,
        "messages": [
            {"type": "text", "text": text}
        ]
    }

    requests.post("https://api.line.me/v2/bot/message/reply", headers=headers, json=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
