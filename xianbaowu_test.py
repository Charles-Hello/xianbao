
from bs4 import BeautifulSoup
import asyncio
import sys
import os
import json
import re
from config import xianbaowuPrevious_titles_file
from http_utilsja2 import AsyncHttpx
from datetime import datetime,timedelta


async def getdetail(id):
    response = await AsyncHttpx.get(f'https://www.hxm5.com/t/{id}')
    return response.text

async def get_htmlids():
    response = await AsyncHttpx.get('https://www.hxm5.com/xianbao/2/')
    return response.text
  

async def capture_redirect_url(url):
    response = await AsyncHttpx.get(url)
    if response.status_code == 200:  
        redirected_url = response.request.url
        return redirected_url  # 返回捕获到的重定向链接
    else:
        print(response.headers)
        return None  # 如果没有重定向，则返回None
      

async def test():

    data_entry = {}

    titleid = '2307957'

    detail_html = await getdetail(titleid)



    #获取正文
    soup = BeautifulSoup(detail_html, 'html.parser')
    text = soup.find_all('p')
    content = ''
    for i in text:
      _content = i.get_text().replace("\n",'')
      _content = _content.replace(" ","")
      content+=_content
      
    #提取图片
    imglist = soup.p.find_all('img')

    if len(imglist) > 0:
      data_entry['ret_images'] = []
      for index, image in enumerate(imglist):
          if 'gif' not in image:
              filename = image['data-original'].rsplit('/', 1)[-1]
              print(image)
              print(f"图片{index+1}:{filename}")
              data_entry['ret_images'].append(
                  {'url': image['data-original'], 'filename': filename})
    else:
      print("没有图片")


    data_entry['ret_content'] = ""
    a_tag = soup.p.find_all('a')
    print(a_tag)
    # print(type(a_tag))
    if  a_tag :
      data_entry['ret_content'] += f"[福]超链接[福]\n"
      for i in a_tag:
        title = ""
        if {"美团", "外卖"} & set(title):
            data_entry['ret_content'] += f"#小程序://美团丨外卖美食买菜酒店电影购物/bgrCmX6IfqoKkLy\n\n"
            break
        link = i['href']
        _redirect_raw_url = f"https://www.hxm5.com{link}"
        redirect_raw_url = await capture_redirect_url(_redirect_raw_url)   
        if 'u.jd.com' in redirect_raw_url or 'coupon' in redirect_raw_url:
            return #广告#
        data_entry['ret_content'] += f"{_redirect_raw_url}\n\n"
    else: 
      print("无超链接")
      
      
      
      
asyncio.run(test())