
import asyncio
import sys
import os
import json
from bs4 import BeautifulSoup
from config import transferurl

# # 获取当前文件的目录路径
# current_dir = os.path.dirname(os.path.abspath(__file__))
# # 获取 http_utils 所在的目录路径
# parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
# # 将 http_utils 所在的目录路径添加到 sys.path 中
# sys.path.append(parent_dir)
from http_utilsja2 import AsyncHttpx



async def getdetail(detail_itemid):
    cookies = {
        'PHPSESSID': 'vsduhtu8brmacg94tajustmp67',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; 22041211AC Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 MAGAPPX|5.9.0-6.5-129|Android 13 Redmi 22041211AC|xiaodigu|ZLeTO8A4K7gDAJ8hb5SA1pc3|ee8c07b7ffb238d90d91161db08c9315|995c53f647964d04fc1f165edbb92456',
        'mag-version': 'Android-5.9.0-6.5-129',
        'mag-ss-key': 'oNv9TMQQR+ISFX61kD4SmlN455GfVzcusUrinqCeEa0L6WrySWjptMfgG836gP9sq6LRpSzmFNqHE4jWwLDzRLIylDSCalg17Va91+n/aiBbvN3deRUPcjvyic991pP7x6ejfHswS5LatW4ClAUQ+Z8AGeoyHAkW9qA5WXcx2rg=',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'app.xiaodigu.cn',
        'Connection': 'Keep-Alive',
    }

    data = {
        'content_id': detail_itemid,
    }
    
    response = await AsyncHttpx.post('https://app.xiaodigu.cn/mag/circle/v3/show/showView', cookies=cookies, headers=headers, data=data)
    
    data =  response.json()
    print("报错位置:")
    print(data)
    data = data['show']

    # print(response.text)

    # response.encoding = 'utf-8'

    # # 假设 response.text 包含 JSON 格式数据
    # data = json.loads(response.text)

    # with open("详情.json", "w", encoding="utf-8") as f:
    #     f.write(json.dumps(data, ensure_ascii=False))  # ensure_ascii=False 禁止使用转义字符
        
    
    
    
    
    title = data['content'][0]
    
    soup = BeautifulSoup(title.replace("\\",""), 'html.parser')
    
    title = soup.get_text()

    print("原来标题："+title)
    
    
    photoslist =[]
    photos = data['pics_arr']
    for item in photos:
        before_url = item['tburl']
        before_url = before_url.replace("\\","")
        photoslist.append(before_url)
    print('图片列表：')
    print(photoslist)
    

    rawurl = transferurl+data['sharedata']['linkurl']
    print("原始链接："+rawurl)
    
    
    return title,photoslist,rawurl
  
  
  
# title,photoslist,rawurl = asyncio.run(getdetail("199623"))


# print(title)
# print(photoslist)
# print(rawurl)