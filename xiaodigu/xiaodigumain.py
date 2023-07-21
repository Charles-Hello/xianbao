


import asyncio
import sys
import os
import json
from bs4 import BeautifulSoup
# current_dir = os.path.dirname(os.path.abspath(__file__))
# # 获取 http_utils 所在的目录路径
# parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
# # 将 http_utils 所在的目录路径添加到 sys.path 中
# sys.path.append(parent_dir)
from config import XiaodiguPrevious_titles_file
from xiaodigu.xiangqing import getdetail
from http_utils import AsyncHttpx
from regx_text import check_word_in_text
import re

async def xiaodigu():
    cookies = {
        'PHPSESSID': '11111111111111111111111111',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; 22041211AC Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 MAGAPPX|5.9.0-6.5-129|Android 13 Redmi 22041211AC|xiaodigu|ZLeTO8A4K7gDAJ8hb5SA1pc3|ee8c07b7ffb238d90d91161db08c9315|995c53f647964d04fc1f165edbb92456',
        'mag-version': 'Android-5.9.0-6.5-129',
        'mag-ss-key': 'hVYjom24fl9/uBgK+YBz368+sEK02ocXg5AUZWNv75SLa5/QVpE3Y8siLyA9RJAGgQRRa6jgstpGP0DWR7CKqqmOcWx+Bewc0P/3L3R7kV92IkWsr+ysCfd7SJMr1PvPI/wIXe05URzxqVxbLcKvXMt9L0xUEFlRVkMB2eprBR4=',
        'Host': 'app.xiaodigu.cn',
        'Connection': 'Keep-Alive',
    }

    params = {
        'p': '1',
        'cat_id': '122',
        'uniqid': '62baa56e56a6e',
        'step': '20',
        'channel_id': '44',
        'is_app_first': '1',
    }

    response = await AsyncHttpx.get(
        'https://app.xiaodigu.cn/mag/info/v2/channel/infoListByCatId',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    # response.encoding = 'utf-8'

    # # 假设 response.text 包含 JSON 格式数据
    # data = json.loads(response.text)

    # with open("listchanel.json", "w", encoding="utf-8") as f:
    #     f.write(json.dumps(data, ensure_ascii=False))  # ensure_ascii=False 禁止使用转义字符
    
    
    if response.status_code == 200:
        data = response.json()
        try:
            with open(XiaodiguPrevious_titles_file, 'r') as file:
                previous_ids = file.read().splitlines()
        except FileNotFoundError:
            # 如果文件不存在，则创建文件并将先前的id列表设置为空列表
            with open(XiaodiguPrevious_titles_file, 'w') as file:
                previous_ids = []

        current_ids = []
        
        postlist = data['list']
        
        for items in postlist:
            detail_items = items['type_value']
            current_ids.append(detail_items)


        new_ids = list(set(current_ids) - set(previous_ids))
        
        # print(new_ids)
        # 将新的id列表保存到txt文件
        with open(XiaodiguPrevious_titles_file, 'w+') as file:
            file.write('\n'.join(current_ids))
        
        listdata = []
        if new_ids:
            indexes = [current_ids.index(new_id) for new_id in new_ids]
            for new_id, index in zip(new_ids, indexes):
                data_entry = {}
                data_entry['new_id'] = new_id 
                print(f"小嘀咕新id: {new_id}, 索引: {index}")
                data  = postlist[index]
                
                
                detail_items = data['type_value']
                title,ret_images,rawurl = await getdetail(detail_items)
                

                result = check_word_in_text(title)
                if not result:
                    print("我被过滤啦")
                    continue  
                    
                data_entry['ret_content'] = f"[庆祝]线报标题[庆祝]\n{title}\n\n[爆竹]线报原始链接[爆竹]\n{rawurl}"
                
                

                data_entry['ret_images'] = []
                for index,image in enumerate(ret_images):
                    if 'gif' not in image:
                        filename = image.rsplit('/', 1)[-1]
                        print(image)
                        print(f"图片{index+1}:{filename}")
                        data_entry['ret_images'].append({'url': image, 'filename': filename})

                listdata.append(data_entry)
                print("====================================="),
            print(listdata)
            return listdata
        else:
            print("没有新的id,无需推送")

    else:
        print("无效请求")

    
    
asyncio.run(xiaodigu())
