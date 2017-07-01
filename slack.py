# パラメータの指定のしやすさなどからrequestsモジュールを使うことにした
import requests
payload = {
    "token": "",
    "channel" : "bot-test",
    "text" : "Hello",
    "username" : "py-bot",
    "pretty" : "1"
}

url = "https://slack.com/api/chat.postMessage"
res = requests.post(url, params=payload)
print(res)
