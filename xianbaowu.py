from bs4 import BeautifulSoup
import asyncio
import sys
import os
import json
import re
from config import xianbaowuPrevious_titles_file
from http_utilsja2 import AsyncHttpx
from regx_text import check_word_in_text
from redislock import createlock,check_lock_existence
from withfilelock import write_current_ids,file_previous_ids
from logreview import debugfilesave
import traceback


async def getdetail(id):
    response = await AsyncHttpx.get(f'https://www.hxm5.com/t/{id}')
    return response.text

async def get_htmlids():
    response = await AsyncHttpx.get('https://www.hxm5.com/xianbao/2/')
    return response.text
  
  
# 文件路径
file_path = xianbaowuPrevious_titles_file
previous_ids,lock = file_previous_ids(file_path)
if not lock:
    exit()
async def hxm5():
  try:
      LOCKstatus =False
      htmlnames = await get_htmlids()
      soup = BeautifulSoup(htmlnames, 'html.parser')
      current_ids = []
      # 提取html的id
      titles = soup.find_all('a')
      dict_data = {}
      
      for i in titles:
          if "title_name" not in str(i):
              continue
          
          htmlid = i['href'].replace('/t/', '')
          # print("id："+htmlid)
          
          title = i['title']
          dict_data[title] = htmlid
          # print("标题："+title)
          current_ids.append(str(title))

      new_ids = list(set(current_ids) - set(previous_ids))
      
          
      listdata = []
      if new_ids:
          #这里写入完毕。解锁
          write_current_ids(file_path, current_ids,lock)
          LOCKstatus =True
          
          
          for new_id in new_ids:
              data_entry = {}
              data_entry['new_id'] = new_id
              index = dict_data[new_id]
              print(f"线报物新id: {new_id}, 索引: {index}")
              
              title =new_id
              titleid = index
              print("title文本:", title)
              if title == "":
                  return
              result = check_word_in_text(title)
              if not result:
                  print("我被过滤啦")
                  continue
              
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
                    link = i['href']
                    data_entry['ret_content'] += f"https://www.hxm5.com/{link}\n\n"
              else:
                  print("无超链接")

              logtime = debugfilesave(detail_html)
              
              rawurl = f"https://www.hxm5.com/t/{titleid}"
              data_entry['ret_content'] += f"[庆祝]线报内容[庆祝]\n{title}\n{content}\n\n[爆竹]线报原始链接[爆竹]\n{rawurl}\n\n✨Debug编号✨\n{logtime}"
              listdata.append(data_entry)
              print("====================================="),
          if listdata:
              print(listdata)
          else:
              print("内容都被过滤掉了")
          return listdata
      else:
          print("没有新的id,无需推送")
          
  except Exception as e:
      print("报错内容：")
      print(e)

      print(traceback.format_exc())
  finally:
      if not LOCKstatus:
          res = check_lock_existence(file_path)
          if res:
              lock.release()
              print('线报屋最后解开锁钥匙')
        
# html = asyncio.run(hxm5())

