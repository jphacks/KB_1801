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

from linebot.models import ImageSendMessage

app = Flask(__name__)

# line_bot_api = LineBotApi('n73xhxL3VDUkyZO8n+AglHevIjEFHfu0nVLJw7v0+ClS0KUp/wMCTlgVtymvhOUbO1/KTNuHkrfVXkSibPsgwF9l/37HNflcUK0nkUwm558oBYFrkaUmwhKILGZwwn2k6PDutmv3W6KXvKmLsVaSjAdB04t89/1O/w1cDnyilFU=')
# handler = WebhookHandler('26527dbb70254d7bef6bcf70669611cf')

line_bot_api = LineBotApi('x4pWezs53vE0b0m+GLVI/c3/yu9VLshsmSbUoKNSjxtt7xxdwDpUNrs9aSxchlHv9bvWvLatf2PHRLQnZnObvAaDHdfX+PPCNzrmdfcXc9DnKedEJBmX6NwVvyVr8bkkX1nuTJmPhtWHa3X37h/2nwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3512a6339b8813c43b290be6d2b578d7')

#@app.route("/callback", methods=['POST'])
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



#使うイメージの読みこみ
def make_image_message():
    messages = ImageSendMessage(
        # original_content_url="https://illust.download/wp-content/uploads/edd/2015/12/person10-1415x1000.jpg", #JPEG 最大画像サイズ：240×240 最大ファイルサイズ：1MB(注意:仕様が変わっていた)
        original_content_url="https://dotup.org/uploda/dotup.org1671762.jpg", #JPEG 最大画像サイズ：240×240 最大ファイルサイズ：1MB(注意:仕様が変わっていた)
        # preview_image_url="https://illust.download/wp-content/uploads/edd/2015/12/person10-1415x1000.jpg" #JPEG 最大画像サイズ：1024×1024 最大ファイルサイズ：1MB(注意:仕様が変わっていた)
        preview_image_url="https://dotup.org/uploda/dotup.org1671762.jpg" #JPEG 最大画像サイズ：1024×1024 最大ファイルサイズ：1MB(注意:仕様が変わっていた)
    )
    return messages


# #push通知したい######################################
import push

file_name = "./flags"
# print(file_name)
# push.doPush()

# file = open(file_name)
# data = file.read()
# print(data)
# if int(data) == 1:
#     print("aaa")
#     # push.doPush()

# try:
#     file = open(file_name)
#     data = file.read()
#     print(data)
# except Exception as e:
#     print(e)
# finally:
#     if int(data) == 1:
#         push.doPush()

# import json
# import requests

# # HTTPヘッダを設定
# HEADERS = {
#     'Content-Type': 'application/json',
#     # 'Authorization': 'Bearer ' + 'n73xhxL3VDUkyZO8n+AglHevIjEFHfu0nVLJw7v0+ClS0KUp/wMCTlgVtymvhOUbO1/KTNuHkrfVXkSibPsgwF9l/37HNflcUK0nkUwm558oBYFrkaUmwhKILGZwwn2k6PDutmv3W6KXvKmLsVaSjAdB04t89/1O/w1cDnyilFU=',
#     'Authorization': 'Bearer ' + 'x4pWezs53vE0b0m+GLVI/c3/yu9VLshsmSbUoKNSjxtt7xxdwDpUNrs9aSxchlHv9bvWvLatf2PHRLQnZnObvAaDHdfX+PPCNzrmdfcXc9DnKedEJBmX6NwVvyVr8bkkX1nuTJmPhtWHa3X37h/2nwdB04t89/1O/w1cDnyilFU=',
# }

# # POSTデータを設定
# POST = {
#     # "to": "U4e960c5ab25f8b111b22de6d7b3fdac0",
#     "to": "U1c98cef02fd67df0ae9b73354d689ba6",
#     "messages": [
#         {
#             'type': 'text',
#             'text': 'hello world'
#         }
#     ]
# }

# # 実行
# CH = 'https://api.line.me/v2/bot/message/push'
# REQ = requests.post(CH, headers=HEADERS, data=json.dumps(POST))

# # HTTPステータスが 200 だったら OK
# print(REQ.status_code)
# if REQ.status_code != 200:
#     print(REQ.text)
# #####################################



@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.type == "message":
        if event.message.type == "text":
            profile = line_bot_api.get_profile(event.source.user_id)
            displayName = profile.display_name

            if event.message.text == u"片付いてる？":
                line_bot_api.reply_message(
                    event.reply_token,
                    [
                        TextSendMessage(text='こんにちは！' + displayName + 'さん' + 'こんな感じ！！' ),
                        make_image_message(),
                    ]
                )
            else:
                line_bot_api.reply_message(
                    event.reply_token,
                    [
                        TextSendMessage(text="「片付いてる？」って聞いてくれへん？"),
                        StickerSendMessage(package_id=1, sticker_id=4),
                    ]
                )

if __name__ == "__main__":
    app.run(host='localhost', port=3000)
