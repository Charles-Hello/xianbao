import re

def check_word_in_text(text):
    word_list = ['?']  # 添加其他关键词到这里
    escaped_words = [re.escape(word) for word in word_list]
    pattern = '|'.join(escaped_words)

    # 使用负向断言排除链接中的?
    pattern = f"(?!https?://)(?:{pattern})"
    
    regex = re.compile(pattern)
    match = regex.search(text)
    if match:
        print(f"匹配到关键词: {match.group()}")
        return False
    else:
        return True

# 测试
text1 = "这是一个测试文本，包含一个关键词"
text2 = "这是另一个测试文本，没有关键词https://example.com/test?param=1"
print(check_word_in_text(text1))
print(check_word_in_text(text2))
