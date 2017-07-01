# requestsモジュールの機能を使ってPOST送信する
# 事前に`pip install requests`
import requests

payload ={
    "token" : "",
    "pretty" : "1"
}

url = "https://slack.com/api/auth.test"

res = requests.post(url, params=payload)

print(res.text)
