# パラメータの指定のしやすさなどからrequestsモジュールを使うことにした
import requests
import json

payload = {
    "token": "",
    "channel": "bot-test",
    "as_user": "false",
    "icon_url": "https://avatars1.githubusercontent.com/u/10055293?v=3&u=1d1491fc3c27e10e93cc364ee0556a3b768c29b2&s=100",
    "text": "attachments test",
    "username": "py-bot",
    "pretty": "1",
    "attachments": json.dumps([
        {
            "fallback": "This is test attachment",
            # "pretext": "これがpretext",
            "title": "TEST",
            "title_link": "http://qiita.com/daikiojm",
            "text": "test:goode",
            "color": "good",
            "author_name": "daikiojm",
            "author_link": "http://qiita.com/daikiojm",
            "author_icon": "https://avatars1.githubusercontent.com/u/10055293?v=3&u=1d1491fc3c27e10e93cc364ee0556a3b768c29b2&s=100",
            "thumb_url": "https://qiita-image-store.s3.amazonaws.com/0/79414/741aebb5-d320-4eb1-f765-59d462f32515.png",
            "footer": "Send from Python",
            "footer_icon": "https://avatars1.githubusercontent.com/u/10055293?v=3&u=1d1491fc3c27e10e93cc364ee0556a3b768c29b2&s=100",
            "ts": "1498894191",
        }
    ])
}


url = "https://slack.com/api/chat.postMessage"
res = requests.post(url, params=payload)
print(res)
