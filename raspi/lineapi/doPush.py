import json
import requests

def doPushMsg(msg):
	# HTTPヘッダを設定
	HEADERS = {
		'Content-Type': 'application/json',
		# 'Authorization': 'Bearer ' + 'n73xhxL3VDUkyZO8n+AglHevIjEFHfu0nVLJw7v0+ClS0KUp/wMCTlgVtymvhOUbO1/KTNuHkrfVXkSibPsgwF9l/37HNflcUK0nkUwm558oBYFrkaUmwhKILGZwwn2k6PDutmv3W6KXvKmLsVaSjAdB04t89/1O/w1cDnyilFU=',
		'Authorization': 'Bearer ' + 'x4pWezs53vE0b0m+GLVI/c3/yu9VLshsmSbUoKNSjxtt7xxdwDpUNrs9aSxchlHv9bvWvLatf2PHRLQnZnObvAaDHdfX+PPCNzrmdfcXc9DnKedEJBmX6NwVvyVr8bkkX1nuTJmPhtWHa3X37h/2nwdB04t89/1O/w1cDnyilFU=',
	}

	# POSTデータを設定
	POST = {
		# "to": "U4e960c5ab25f8b111b22de6d7b3fdac0",
		"to": "U1c98cef02fd67df0ae9b73354d689ba6",
		"messages": [
			{
					'type': 'text',
					# 'text': 'hello world'
					'text': msg
			}
		]
	}

	# 実行
	CH = 'https://api.line.me/v2/bot/message/push'
	REQ = requests.post(CH, headers=HEADERS, data=json.dumps(POST))

	# HTTPステータスが 200 だったら OK
	print(REQ.status_code)
	if REQ.status_code != 200:
		print(REQ.text)
	#####################################