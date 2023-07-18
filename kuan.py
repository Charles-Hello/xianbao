
from config import kuanPrevious_ids_file,user_id,test_room
from bs4 import BeautifulSoup
from get_url_content import get_url_images
import re
from http_utils import AsyncHttpx
import asyncio
from push import send_text_msg,SendImageMsg
from regx_text import check_title_and_content

async def kuan_hot():


    response = await AsyncHttpx.get('http://new.ixbk.net/category-kuan/', verify=False)

    response.encoding = 'utf-8'

    if response.status_code == 200:
        try:
            with open(kuanPrevious_ids_file, 'r') as file:
                previous_ids = file.read().splitlines()
        except FileNotFoundError:
            # 如果文件不存在，则创建文件并将先前的id列表设置为空列表
            with open(kuanPrevious_ids_file, 'w') as file:
                previous_ids = []

        current_ids = []
        soup = BeautifulSoup(response.text, 'html.parser')
        div_content = soup.find_all('p', class_='title')
        for i in div_content:
            a_tag = i.find('a')
            if a_tag:
                pattern = r'href="/kuan/(.*?).html"\s+target='
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
        with open(kuanPrevious_ids_file, 'w+') as file:
            file.write('\n'.join(current_ids))
        if new_ids:
            indexes = [current_ids.index(new_id) for new_id in new_ids]
            for new_id, index in zip(new_ids, indexes):
                print(f"酷安id: {new_id}, 索引: {index}")
                data  = div_content[index].find('a')
                title = data.get('title')
                content = data.get('data-content')
                url = data.get('href')
                print("Title:", title)
                print("Content:", content)
                result = check_title_and_content(title, content)
                if not result:
                    print("我被过滤啦")
                    continue
                # print("URL:", url)
                ret_content = f"[庆祝]线报标题[庆祝]\n{title}\n\n[烟花]推送内容[烟花]\n{content}"
                pattern = r'/kuan/(.*?).html'
                match = re.search(pattern, str(url))
                if match:
                    extracted_content = match.group(1)
                    ret_url,ret_images = await get_url_images("kuan",extracted_content)
                    if ret_url:
                        ret_content+=f"\n\n[福]超链接[福]\n{ret_url}"
                        print(ret_content)
                        print(ret_images)
                else:
                    print("没有匹配到URL内容")
                    
                await send_text_msg(user_id,test_room,f'{ret_content}')
                if ret_images:
                    for index,image in enumerate(ret_images):
                        if 'gif' not in image:
                            filename = image.rsplit('/', 1)[-1]
                            print(image)
                            print(f"图片{index+1}:{filename}")
                            await SendImageMsg(user_id,test_room,image,f'{filename}')
                print("====================================="),
            return ret_content,ret_images
        else:
            print("没有新的id,无需推送")
    else:
        print('请求失败')
        








