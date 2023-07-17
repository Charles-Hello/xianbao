


# previous_ids = [1,2,4]
# current_ids = [1,2,3]
# new_ids = list(set(current_ids) - set(previous_ids))
# # 查找新的id在先前列表的索引
# indexes = [current_ids.index(new_id) for new_id in new_ids]

# print("新id在先前列表的索引：")
# for new_id, index in zip(new_ids, indexes):
#     print(f"新id: {new_id}, 索引: {index}")

import re
text = '<p>https://ks.wjx.top/vm/rtx63DO.aspx!!收拾收拾<meta'
# pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
# urls = re.findall(pattern, text)
# print(urls)

import re

# text = "这是一段包含URL链接的文本，例如：https://www.example.com 和 http://anotherlink.com"

# 定义URL匹配模式的正则表达式（非贪婪模式）
url_pattern = re.compile(r"https?://\S+")

# 使用findall函数提取文本中的所有URL链接
urls = re.findall(url_pattern, text)

# 去除链接后面的特殊内容
cleaned_urls = [re.match(r"(.*?)(?:<|$)", url).group(1) for url in urls]
print(cleaned_urls)
if cleaned_urls:
    # 打印提取到的URL链接
    for url in cleaned_urls:
        print(url)