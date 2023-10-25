import requests
import json
from tomd import Tomd
from time import sleep
import logging
from urllib3 import disable_warnings
import time

disable_warnings()
logging.basicConfig(filename='MB.log', level=logging.INFO)

header = {
    "Authorization": "Bearer eyJhbGciOiJFUzUxMiJ9"
                     ".eyJ1c2VyX2lkIjoxMzA1MDE5NSwidXNlcl9wb3J0YWxfYWNjb3VudF9pZCI6ImRwNldyWUZueHdBdWlWZzE1ZEhHejcxUCIsImVtYWlsIjoicGFuLndlbnl1YW4uMjNAamRmemliLm9yZyIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJtYW5hZ2ViYWMifQ.AKSWmAW2C32I1irpWsJaKhRCzj3EOksg7c3MyO7E6JfgVvM7RBwuGqqJDzB1e-QAkWeeFycy4s6Vaz6wtKXmK6cSAQeOrt1ZuLCQqFXFHjMpw124gzYvxbecDOo083a1Y7c7ieFJHTfgiGTw8SfeMsQopNF-0wdMGm9z-sbYq1D9Z17o"}
webhook = ("https://oapi.dingtalk.com/robot/send?access_token"
           "=15d1c0e7e41b878862141399d2f8b310f86e1a7bd9091481611f326a3966d337")
loop_times = 0
logging.info("config finished, start to loop")
while True:
    loop_times += 1
    unread_msg_num = 0
    req = requests.get("https://mnn-hub.prod.faria.cn/api/frontend/notifications?page=1", headers=header, verify=False)
    content = req.content.decode("utf-8")
    notice_dict = json.loads(content)
    for c in notice_dict["notifications"]:
        if c["is_read"]:
            continue
        unread_msg_num += 1
        tomd_obj = Tomd(c["body"])
        md = tomd_obj.markdown
        webhook_msg = {
            "msgtype": "markdown",
            "markdown": {
                "title": "MB通知",
                "text": str(md)+"欸嘿"
            }
        }
        qq_msg = {
            "group_id": 392474787,
            "message": md
        }
        webhook_resp = requests.post(webhook, json=webhook_msg, verify=False)
        print(webhook_resp.content)
        req = requests.put("https://mnn-hub.prod.faria.cn/api/frontend/v2/notifications/mark_as_read", headers=header, verify=False, data={"ids": "all"})
        print(req.content)
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    logging.info(f"loop {loop_times} at {current_time} finished, found {unread_msg_num} message unread")
    sleep(20)
