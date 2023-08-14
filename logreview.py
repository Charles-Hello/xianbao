
import json
import datetime
import os
from bs4 import BeautifulSoup

def is_html(text):
    try:
        soup = BeautifulSoup(text, 'html.parser')
        return True
    except:
        return False

def debugfilesave(data):
  try:
      # 获取当前时间
      current_time = datetime.datetime.now()

      # 生成文件名
      if not is_html(data):
          # 将 JSON 数据保存到 JSON 文件中
          file_name = current_time.strftime("%Y-%m-%d-%H-%M-%S.json")
          with open(file_name, 'w',encoding='utf-8') as json_file:
              json.dump(data, json_file, indent=4,ensure_ascii=False)
      else:
          file_name = current_time.strftime("%Y-%m-%d-%H-%M-%S.html")
          with open(file_name, 'w',encoding='utf-8') as html_file:
              html_file.write(data)

      print(f"Data saved to '{file_name}'.")
      # 删除前7天的 JSON 文件
      delete_old_files()
      return str(current_time.replace(microsecond=0))
  except Exception as e:
      print("debugfilesave出错")
      print(e)
      return str(current_time.replace(microsecond=0))
  
  
def delete_old_files():
    current_time = datetime.datetime.now()
    seven_days_ago = current_time - datetime.timedelta(days=3)

    for file_name in os.listdir('.'):
        if file_name.endswith('.json'):
            if not {"20", "-"} & set(file_name):
                continue
            file_time = datetime.datetime.strptime(file_name[:-5], "%Y-%m-%d-%H-%M-%S")
            if file_time < seven_days_ago:
                os.remove(file_name)
                print(f"Deleted old file: '{file_name}'")

# # 调用 debugfilesave 函数并传入 JSON 数据
# data = {'key': 'value'}
# debugfilesave(data)