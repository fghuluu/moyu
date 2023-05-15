import os
import json
import time
import hmac
import hashlib
import base64
import requests
import urllib.parse

access_token = os.environ.get('access_token')
secret = os.environ.get('secret')
url = 'https://api.vvhan.com/api/moyu'
res = requests.get(url, allow_redirects=False)
img_url = res.headers.get("location")
print(img_url)

timestamp = str(round(time.time() * 1000))
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
print(timestamp)
print(sign)

url = "https://oapi.dingtalk.com/robot/send?access_token="+access_token+"&timestamp="+timestamp+"&sign="+sign
data={
     "msgtype": "markdown",
     "markdown": {
         "title":"摸鱼日历",
         "text": "![screenshot]("+img_url+")\n"
     }
 }
headers = {'Content-Type': 'application/json'}
response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.text)
