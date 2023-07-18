


import re
from http_utils import AsyncHttpx
import asyncio
from tenacity import retry, stop_after_attempt, stop_after_delay, wait_chain, wait_fixed



# @retry(stop=stop_after_attempt(10), wait=wait_fixed(3))
# async def xiaodigu_hot():
#     print(":")
# #     result = 5 / 0
    
# asyncio.run(xiaodigu_hot())


dd =[1,2,3,4,5,6,7,8,9,10,]
print(dd)