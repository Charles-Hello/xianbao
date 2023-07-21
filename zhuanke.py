import re
from get_url_content import get_url_images
from config import zhuanPrevious_ids_file, user_id, test_room
from http_utilsja2 import AsyncHttpx
import asyncio
from push import send_text_msg, SendImageMsg
from regx_text import check_title_and_content


async def zhuanke_hot():
    cookies = {
        'timezone': '8',
    }

    response = await AsyncHttpx.get('http://new.ixbk.net/plus/json/zuan-hot.json',
                                    cookies=cookies,  verify=False)
    # 检查响应是否成功

    if response.status_code == 200:
        # 指定保存的文件路径

        # 读取先前的id列表
        try:
            with open(zhuanPrevious_ids_file, 'r') as file:
                previous_ids = file.read().splitlines()
        except FileNotFoundError:
            # 如果文件不存在，则创建文件并将先前的id列表设置为空列表
            with open(zhuanPrevious_ids_file, 'w') as file:
                previous_ids = []

        current_data = response.json()

        current_ids = [item['title'] for item in current_data['remen6']]
        new_ids = list(set(current_ids) - set(previous_ids))
        # 将新的id列表保存到txt文件
        with open(zhuanPrevious_ids_file, 'w+') as file:
            file.write('\n'.join(current_ids))

        listdata = []
        if new_ids:
            indexes = [current_ids.index(new_id) for new_id in new_ids]
            for new_id, index in zip(new_ids, indexes):
                print(f"赚客新id: {new_id}, 索引: {index}")

                data_entry = {}
                data_entry['new_id'] = new_id
                data = current_data['remen6'][index]
                title = data['title']
                content = data['content']
                url = data['url']
                # print("Title:", title)
                # print("Content:", content)
                # print("URL:", url)
                result = check_title_and_content(title, content)
                if not result:
                    print("我被过滤啦")
                    continue
                data_entry['ret_content'] = f"[庆祝]线报标题[庆祝]\n{title}\n\n[烟花]推送内容[烟花]\n{content}"
                pattern = r"\/zuankeba\/(.*?)\.html"
                match = re.search(pattern, url)
                if match:
                    extracted_content = match.group(1)
                    ret_url, ret_images = await get_url_images("zuankeba", extracted_content)
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
                            # print(image)
                            # print(f"图片{index+1}:{filename}")
                            data_entry['ret_images'].append(
                                {'url': image, 'filename': filename})
                # print("====================================="),
            # print(listdata)
            return listdata
        else:
            print("没有新的id,无需推送")
    else:
        print('请求失败')


# asyncio.run(zhuanke_hot())
