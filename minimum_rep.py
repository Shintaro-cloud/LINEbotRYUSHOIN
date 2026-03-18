from flask import Flask, request, abort
import requests
import os

app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = "eh5UPbWRqIs1yKwaw8jX6T8nb6ev5Kp7voYRc058+T6AYs7fiiRgUyvRi/je8spTf1BeWUdfHJBNmbIk337IvCSLFu/i2q2BBu8y3/QCZd9VdcQlrXmxV4/HFeOluMzpXgziPlf65m3JbGrIgtlHKQdB04t89/1O/w1cDnyilFU="

sticker_responses = {
    "826611625": "本は心の栄養なのですわ♪",
    "826611626": "LINEやりながら勉強なんて嘘ですわ",
    "826611627": "いい加減にしてくださいな。さっさと携帯しまって勉強してくださいな",
    "826611628": "一人で悩むのはたいへんですわ。わたくしが話を聞いて差し上げますわ♪",
    "826611629": "決してぼうりょくではありませんわ♪",
    "826611630": "さすが四郎様！ごうそっきゅうですわ♪",
    "826611631": "ふるすいんぐですわ♪",
    "826611632": "細心の注意ですわ",
    "826611633": "変な花...",
    "826611634": "何を歌っているのですの？",
    "826611635": "聞かせたい人がいるから上達するのですわ♪",
    "826611636": "軽い運動は大事ですわ♪",
    "826611637": "待っている間にお話しいたしませんか？",
    "826611638": "やめられないのですわ...",
    "826611639": "いやん、恥ずかしいですわ～",
    "826611640": "嬉しいですが...わたくしには四郎様がおりますわ...お気持ちにはこたえられませんわ"
}

@app.route("/callback", methods=['POST'])
def callback():
    body = request.json

    for event in body['events']:
        if event['type'] == 'message':
            reply_token = event['replyToken']
            msg_type = event['message']['type']

            if msg_type == "sticker":
                sticker_id = str(event['message']['stickerId'])
                reply_text = sticker_responses.get(sticker_id, "どうも、龍勝院ですわ。")
                reply_message(reply_token, reply_text)
            else:
                reply_message(reply_token, "どうも、龍勝院ですわ。")

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
