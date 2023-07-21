from config import XiaodiguPrevious_ids_file, user_id, test_room
from bs4 import BeautifulSoup
from get_url_content import get_url_images
import re
from http_utilsja2 import AsyncHttpx
import asyncio
from push import send_text_msg, SendImageMsg
from regx_text import check_title_and_content


async def xiaodigu_hot():

    response = await AsyncHttpx.get('http://new.ixbk.net/category-xiaodigu/', verify=False)

    response.encoding = 'utf-8'

    if response.status_code == 200:
        try:
            with open(XiaodiguPrevious_ids_file, 'r') as file:
                previous_ids = file.read().splitlines()
        except FileNotFoundError:
            # 如果文件不存在，则创建文件并将先前的id列表设置为空列表
            with open(XiaodiguPrevious_ids_file, 'w') as file:
                previous_ids = []

        current_ids = []
        soup = BeautifulSoup(response.text, 'html.parser')
        div_content = soup.find_all('p', class_='title')
        for i in div_content:
            a_tag = i.find('a')
            if a_tag:
                pattern = r'title="(.*?)"[^>]*?>'
                match = re.search(pattern, str(a_tag))
                if match:
                    extracted_content = match.group(1)
                    current_ids.append(extracted_content)
                else:
                    print("没有匹配到URL内容")
            else:
                print("没有匹配到a标签")

        new_ids = list(set(current_ids) - set(previous_ids))
        # 将新的id列表保存到txt文件
        with open(XiaodiguPrevious_ids_file, 'w+') as file:
            file.write('\n'.join(current_ids))

        listdata = []
        if new_ids:
            indexes = [current_ids.index(new_id) for new_id in new_ids]
            for new_id, index in zip(new_ids, indexes):
                data_entry = {}
                data_entry['new_id'] = new_id
                print(f"小嘀咕新id: {new_id}, 索引: {index}")
                data = div_content[index].find('a')
                title = data.get('title')
                content = data.get('data-content')
                url = data.get('href')
                # print("Title:", title)
                # print("Content:", content)
                result = check_title_and_content(title, content)
                if not result:
                    print("我被过滤啦")
                    continue
                # print("URL:", url)
                data_entry['ret_content'] = f"[庆祝]线报标题[庆祝]\n{title}\n\n[烟花]推送内容[烟花]\n{content}"
                pattern = r'/xiaodigu/(.*?).html'
                match = re.search(pattern, str(url))
                if match:
                    extracted_content = match.group(1)
                    ret_url, ret_images = await get_url_images("xiaodigu", extracted_content)
                    if ret_url:
                        data_entry['ret_content'] += f"\n\n[福]超链接[福]\n{ret_url}"
                else:
                    print("没有匹配到URL内容")

                listdata.append(data_entry)
                if ret_images:
                    data_entry['ret_images'] = []
                    for index, image in enumerate(ret_images):
                        if 'gif' not in image:
                            filename = image.rsplit('/', 1)[-1]
                            print(image)
                            print(f"图片{index+1}:{filename}")
                            data_entry['ret_images'].append(
                                {'url': image, 'filename': filename})
                print("====================================="),
            return listdata
        else:
            print("没有新的id,无需推送")
    else:
        print('请求失败')


# demo = asyncio.run(xiaodigu_hot())
