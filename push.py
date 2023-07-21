

import ujson
from http_utilsja2 import AsyncHttpx
from config import *


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
    return await AsyncHttpx.post(url=API_URL, data=result, headers=headers, tls=False)


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
    await AsyncHttpx.post(url=API_URL, data=data, headers=headers, timeout=None, tls=False)


# url = 'http://image.coolapk.com/feed/2023/0720/23/802421_be548e77_5582_6952_395@1440x3200.jpeg'
# name = '6952_395@1440x3200.jpeg'
# import asyncio
# asyncio.run(SendImageMsg(user_id,tnanko,url,name))
# # # asyncio.run(send_text_msg(user_id,tnanko,name))
