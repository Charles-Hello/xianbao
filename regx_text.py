import re


word_list = ['求', '话说', '问', '麻烦', '如题', '求助', '大神', '求解', '呢', '怎样', '吗', '?', '？', '状态', '如何', '哪里', '哪儿', '帮忙',
             '哪个', '哪些', '哪种', '哪样', '哪位', '哪家', '哪边',  '建议', '有没有', '直播', '黄了', '啥', '不知道', '是否', '碎碎念',  '才能','怎么', '如何', '什么', '哪里', '哪儿',  '哪些', '哪种', '哪样', '哪位', '哪家', '哪边', '几时', '多久', '多少', '多大', '多高', '多远', '多宽', '多重', '多长', '多快', '吗', '是否', '难道', '岂不是', '是不是', '难道不是', '难道不会', '不是吗', '不会吧', '还是', '或者', '难道要', '能否', '可否', '会不会',  '有无', '能不能', '能够', '能不能够', '可不可以', '可不', '是吧', '是不是啊', '难道是', '应该', '大概', '大约', '可能', '或许', '恐怕', '大概是', '可能是', '或许是', '恐怕是','咋回事儿','都没有','推荐','医院','机器人','代跑','废物',"鱼","收",'抢不到','糖分','注意身体','安全','自动评价','去广告','去更新','违约','妈的','起诉','稳否','咨询','请教','私聊','交作业','老赖','代下','血亏','曝光','骗子','骚扰','禁止','互助','组队','重复']


def check_word_in_text(text):
    escaped_words = [re.escape(word) for word in word_list]
    pattern = '|'.join(escaped_words)
    regex = re.compile(pattern)
    match = regex.search(text)
    if match:
        return False
    else:
        return True



def check_title_and_content(title, content):
    title_check = check_word_in_text(title)
    content_check = check_word_in_text(content)
    return title_check and content_check
