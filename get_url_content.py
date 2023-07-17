from bs4 import BeautifulSoup
import re
from http_utils import AsyncHttpx


async def get_url_images(type, number):
  
  
    ret_url = ""
    ret_images =[]
    cookies = {
        'timezone': '8',
    }

    response = await AsyncHttpx.get(
        f'http://new.ixbk.net/{type}/{number}.html', cookies=cookies, verify=False)
    response.encoding = 'utf-8'
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    div_content = soup.find('div', class_='article-content')
    pattern = r'src="(.*?)"\s+title='
    matchs = re.findall(pattern, str(div_content))
    if matchs:
        for index,match in enumerate(matchs):
            # print(f"第{index}的图片：{match}")
            ret_images.append(match)
    else:
        print("没有匹配到URL的src内容")
        
        
    #超链接提取
    urlpattern = r'href="(.*?)"\s+target='
    matchs = re.findall(urlpattern, str(div_content))
    if matchs:
         for index,match in enumerate(matchs):
              ret_url+=match+"\n"
              print(f"第{index}的超链接：{match}")
    else:
        url_pattern = re.compile(r"https?://\S+")
        # 使用findall函数提取文本中的所有URL链接
        urls = re.findall(url_pattern, str(div_content))
        # 去除链接后面的特殊内容
        cleaned_urls = [re.match(r"(.*?)(?:<|$)", url).group(1) for url in urls]
        if cleaned_urls:
            if not re.search(r'jpg|jpeg|png|gif|mp3|mp4|wav', str(cleaned_urls)):
                for url in cleaned_urls:
                    ret_url+=url+"\n"

    #返回url或者图片
    return ret_url,ret_images