


from xiaodigu import xiaodigu_hot
from zhuanke import get_hot as zhuanke_hot
import asyncio
from push import send_text_msg,SendImageMsg
from config import user_id,test_room

'''
cron: * * * * *
new Env('push线报');
'''


async def main():
    tasks = [
        xiaodigu_hot(),
        zhuanke_hot(),
        # 添加其他需要运行的异步方法
    ]
    results =await asyncio.gather(*tasks)
    # for i in results:
    #     if i:
    #         result = i[0]
    #         print(result)
    #         await send_text_msg(user_id,test_room,f'{result}')
    #         if i[1]:
    #             for index,image in enumerate(i[1]):
    #                 if 'gif' not in image:
    #                     filename = image.rsplit('/', 1)[-1]
    #                     print(image)
    #                     print(f"图片{index+1}:{filename}")
    #                     await SendImageMsg(user_id,test_room,image,f'{filename}')
    #         print("====================================="),


if __name__ == '__main__':
    asyncio.run(main())