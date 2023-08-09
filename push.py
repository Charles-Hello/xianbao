

import ujson
from http_utilsja2 import AsyncHttpx
from config import *
import requests

headers = {
    'Name': 'iHttp',
    'Ver': "1.1.6.1",
    'Udid': '0b4891edc500803721b76cf782200fd3',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76',
}


async def send_text_msg(robot_wxid, to_wxid, msg):
    data = dict()
    data["event"] = "SendTextMsg"
    data["robot_wxid"] = robot_wxid
    data["to_wxid"] = to_wxid
    data["msg"] = msg
    result = ujson.dumps(data)
    return requests.post(url=API_URL, data=result, headers=headers)


async def send_text_msg1(msg,group_id):

    payload = ujson.dumps({
      "action": "send_message",
      "params": {
          "detail_type": "group",
          "group_id": group_id,
          "message": [
            {
                "type": "text",
                "data": {
                  "text": msg
                }
            }
          ]
      }
    })

    requests.post(API_URL, headers=headers, data=payload)


async def SendImageMsg(robot_wxid, to_wxid, path, name):
    data = dict()
    msg = dict()
    data["event"] = "SendImageMsg"
    data["robot_wxid"] = robot_wxid
    data["to_wxid"] = to_wxid
    msg["url"] = path
    msg['name'] = name
    data['msg'] = msg
    data = ujson.dumps(data)
    return requests.post(url=API_URL, data=data, headers=headers, timeout=None)



async def SendImageMsg1(url, group_id):
    payload = ujson.dumps({
      "action": "upload_file",
      "params": {
          "type": "url",
          "name": "logo.jpg",
          "url": url
      }
    })
    response = requests.post(API_URL, headers=headers, data=payload)
    data = response.json()
    fileid= data['data']['file_id']


    payload = ujson.dumps({
      "action": "send_message",
      "params": {
          "detail_type": "group",
          "group_id":group_id,
          "message": [
            {
                "type": "image",
                "data": {
                  "file_id": fileid
                }
            }
          ]
      }
    })

    response = requests.post(API_URL, headers=headers, data=payload)

    print(response.text)
