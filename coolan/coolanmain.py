import asyncio
import sys
import os
import json
import re


from bs4 import BeautifulSoup
from coolan.coolanutils import cool_market_headers
from config import kuandiguPrevious_titles_file
from http_utilsja2 import AsyncHttpx
from regx_text import check_word_in_text
from redislock import createlock
from withfilelock import write_current_ids,file_previous_ids

# 文件路径
file_path = kuandiguPrevious_titles_file
previous_ids = file_previous_ids(file_path)


async def kuan():

    params = {
        'url': '#/feed/multiTagFeedList?listType=dateline_desc&hiddenTagRelation=1&tag=%E8%96%85%E7%BE%8A%E6%AF%9B%E5%B0%8F%E5%88%86%E9%98%9F',
        'title': '最新发布',
        'subTitle': '',
        'page': '1',
    }
    response = await AsyncHttpx.get('https://api.coolapk.com/v6/page/dataList', params=params, cookies=cool_market_headers.cookies, headers=cool_market_headers.headers)
    if response.status_code == 200:
        # print(response.text)

        # response.encoding = 'utf-8'

        # # 假设 response.text 包含 JSON 格式数据
        # data = json.loads(response.text)

        # with open("kuan.json", "w", encoding="utf-8") as f:
        #     f.write(json.dumps(data, ensure_ascii=False))  # ensure_ascii=False 禁止使用转义字符
        data = response.json()
        # print(data)



        current_ids = []

        postlist = data['data']

        for items in postlist:
            # print(items)
            if 'message' in items:
                detail_items = items['message']
                # print(detail_items)
            else:
                break
            soup = BeautifulSoup(detail_items, 'html.parser')
            non_html_text = soup.get_text()
            non_html_text = non_html_text.replace("查看链接", "").replace('#薅羊毛小分队#', '').replace('\n', '')
            current_ids.append(str(non_html_text))

        new_ids = list(set(current_ids) - set(previous_ids))

        # print(new_ids)
        

        listdata = []
        if new_ids:
            write_current_ids(file_path, current_ids)
            #这里写入完毕。解锁
            indexes = [current_ids.index(new_id) for new_id in new_ids]
            for new_id, index in zip(new_ids, indexes):
                data_entry = {}
                data_entry['new_id'] = new_id
                print(f"酷安新id: {new_id}, 索引: {index}")
                data = postlist[index]
                # print(data)
                message = data['message']
                soup = BeautifulSoup(message, 'html.parser')
                non_html_text = soup.get_text()
                non_html_text = non_html_text.replace(
                    "查看链接", "").replace('#薅羊毛小分队#', '').replace('\n', '')
                print("non_html_text文本:", non_html_text)
                if non_html_text == "":
                    return
                result = check_word_in_text(non_html_text)
                if not result:
                    print("我被过滤啦")
                    continue

                picArr = data['picArr']
                if len(picArr) > 0:
                    data_entry['ret_images'] = []
                    for index, image in enumerate(picArr):
                        if 'gif' not in image:
                            filename = image.rsplit('_', 1)[-1]
                            print(image)
                            print(f"图片{index+1}:{filename}")
                            data_entry['ret_images'].append(
                                {'url': image, 'filename': filename})
                else:
                    print("没有图片")

                data_entry['ret_content'] = ""
                a_tag = soup.find_all('a')
                if a_tag is not None:
                    for i in a_tag:
                        if '薅羊毛小分队' not in i['href']:
                            link = i['href']
                            data_entry['ret_content'] = f"[福]超链接[福]\n{link}\n"
                else:
                    print("无超链接")


                rawurl = data['shareUrl']
                data_entry['ret_content'] += f"[庆祝]线报内容[庆祝]\n{non_html_text}\n\n[爆竹]线报原始链接[爆竹]\n{rawurl}"
                listdata.append(data_entry)
                print("====================================="),
            print(listdata)
            return listdata
        else:
            print("没有新的id,无需推送")

    else:
        print("请求失败")
    lock = createlock(file_path)
    lock.release()
    print('解开锁钥匙')

# asyncio.run(kuan())
