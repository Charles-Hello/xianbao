


from coolan.coolanmain import kuan
from zhuanke import zhuanke_hot
from xiaodigu.xiaodigumain import xiaodigu
import asyncio
from push import send_text_msg,SendImageMsg,send_text_msg1,SendImageMsg1
from config import user_id,test_room
from xianbaowu import hxm5
'''
cron: */10 * * * * *
new Env('push线报');
'''


async def main():
    tasks = [
        xiaodigu(),
        kuan(),
        hxm5(),
        # zhuanke_hot(),todo:暂时不用
        # 添加其他需要运行的异步方法
    ]
    results = await asyncio.gather(*tasks)

    for items in results: 
        if not items:
            continue
        for item in items: 
            new_id = item['new_id']
            ret_content = item['ret_content']
            ret_images = item.get('ret_images', []) 
            print("New ID:", new_id)
            print("Ret Content:", ret_content)
            print("Ret Images:")
            await send_text_msg1(f'{ret_content}',test_room)
            for image in ret_images:
                url = image['url']
                filename = image['filename']
                print("URL:", url)
                print("Filename:", filename)
                await SendImageMsg1(url,test_room)
            print("=====================================")
            await asyncio.sleep(6)

if __name__ == '__main__':
    asyncio.run(main())