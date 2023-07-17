

import ujson
from http_utils import AsyncHttpx
from config import API_URL




headers = {
      'Name': 'iHttp',
      'Ver': "1.1.6.1",
      'Udid': '0b4891edc500803721b76cf782200fd3',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76',
}

async def send_text_msg(robot_wxid, to_wxid, msg):
    print(f"发送消息:{msg}")
    data = dict()
    data["event"] = "SendTextMsg"
    data["robot_wxid"] = robot_wxid
    data["to_wxid"] = to_wxid
    data["msg"] = msg
    result = ujson.dumps(data)
    print(result)
    return await AsyncHttpx.post(url=API_URL, data=result, headers=headers)
  
  
  
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
    await AsyncHttpx.post(url=API_URL, data=data, headers=headers, timeout=None)