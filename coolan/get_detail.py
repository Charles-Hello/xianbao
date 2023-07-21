import asyncio
import sys
import os
import json
from coolan.coolanutils import cool_market_headers
# current_dir = os.path.dirname(os.path.abspath(__file__))
# # 获取 http_utils 所在的目录路径
# parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
# # 将 http_utils 所在的目录路径添加到 sys.path 中
# sys.path.append(parent_dir)

from http_utilsja2 import AsyncHttpx


async def get_detail(id):

    params = {
        'id': id,
        'fromApi': '/v6/search?type=feed&feedType=all&sort=default&searchValue=%E4%BF%9D%E5%BA%95&pageType=tag&pageParam=%E8%96%85%E7%BE%8A%E6%AF%9B%E5%B0%8F%E5%88%86%E9%98%9F&page=1&showAnonymous=-1',
    }

    response = await AsyncHttpx.post('https://api2.coolapk.com/v6/feed/detail', params=params, cookies=cool_market_headers.cookies, headers=cool_market_headers.headers)

    # print(response.text)

    # response.encoding = 'utf-8'

    # # 假设 response.text 包含 JSON 格式数据
    # data = json.loads(response.text)

    # with open("kuandetail.json", "w", encoding="utf-8") as f:
    #     f.write(json.dumps(data, ensure_ascii=False))  # ensure_ascii=False 禁止使用转义字符
    data = response.json()
    message = data['data']['message']
    # print(message)
    return message


# asyncio.run(get_detail("47800794"))
