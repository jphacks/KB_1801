# -*- coding: utf-8 -*-
import sys
sys.path.append('./vendor')

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

from doPush import doPushMsg, doPushImg

app = Flask(__name__)

# line_bot_api = LineBotApi('n73xhxL3VDUkyZO8n+AglHevIjEFHfu0nVLJw7v0+ClS0KUp/wMCTlgVtymvhOUbO1/KTNuHkrfVXkSibPsgwF9l/37HNflcUK0nkUwm558oBYFrkaUmwhKILGZwwn2k6PDutmv3W6KXvKmLsVaSjAdB04t89/1O/w1cDnyilFU=')
# handler = WebhookHandler('26527dbb70254d7bef6bcf70669611cf')

line_bot_api = LineBotApi('x4pWezs53vE0b0m+GLVI/c3/yu9VLshsmSbUoKNSjxtt7xxdwDpUNrs9aSxchlHv9bvWvLatf2PHRLQnZnObvAaDHdfX+PPCNzrmdfcXc9DnKedEJBmX6NwVvyVr8bkkX1nuTJmPhtWHa3X37h/2nwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3512a6339b8813c43b290be6d2b578d7')

doPushMsg("Alart: Clean Yout Desk!!")
doPushImg()