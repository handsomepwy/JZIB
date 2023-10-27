import requests
import json
from tomd import Tomd
from time import sleep
import logging
from urllib3 import disable_warnings
import time
import os

disable_warnings()
logging.basicConfig(filename='MB.log', level=logging.INFO)

header = {
    "Authorization": os.environ["MB_AUTH_VALUE"]}
webhook = (os.environ["DING_WEBHOOK"])
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
        webhook_resp = requests.post(webhook, json=webhook_msg, verify=False)
        print(webhook_resp.content)
        req = requests.put("https://mnn-hub.prod.faria.cn/api/frontend/v2/notifications/mark_as_read", headers=header, verify=False, data={"ids": "all"})
        print(req.content)
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    logging.info(f"loop {loop_times} at {current_time} finished, found {unread_msg_num} message unread")
    sleep(20)
