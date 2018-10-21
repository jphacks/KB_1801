# -*- coding: utf-8 -*-
import sys
sys.path.append('.\\vendor')

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('x4pWezs53vE0b0m+GLVI/c3/yu9VLshsmSbUoKNSjxtt7xxdwDpUNrs9aSxchlHv9bvWvLatf2PHRLQnZnObvAaDHdfX+PPCNzrmdfcXc9DnKedEJBmX6NwVvyVr8bkkX1nuTJmPhtWHa3X37h/2nwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3512a6339b8813c43b290be6d2b578d7')


# @app.route("/callback", methods=['POST'])
@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.type == "message":
        if event.message.type == "text":
            profile = line_bot_api.get_profile(event.source.user_id)
            displayName = profile.display_name

            # print(displayName)

            if event.message.text == u"こんにちは":
                # sys.exit("print")
                line_bot_api.reply_message(
                    event.reply_token,
                    [
                        StickerSendMessage(package_id=1, sticker_id=17),
                        TextSendMessage(text='こんにちは！' + displayName + 'さん')
                    ]
                )
            else:
                line_bot_api.reply_message(
                    event.reply_token,
                    [
                        TextSendMessage(text="「こんにちは」と呼びかけてね！"),
                        StickerSendMessage(package_id=1, sticker_id=4),
                    ]
                )

if __name__ == "__main__":
    app.run(host='localhost', port=3000)
    # sys.exit("error")
