
import re


word_list = ["启动", "调查", '后来', '嘎嘎', '认真', '求', '话说', '问', '麻烦', '如题', '求助', '大神', '求解', '呢', '怎样', '吗', '状态', '如何', '帮忙', '哪', '建议', '有没有', '直播', '黄了', '啥', '不知道', '是否', '碎碎念', '才能', '怎么', '如何', '什么', '几时', '多久', '多少', '多大', '多高', '多远', '多宽', '多重', '多长', '多快', '是否', '难道', '岂不是', '是不是', '难道不是', '难道不会', '不是吗', '不会吧', '还是', '或者', '难道要', '能否', '可否', '会不会', '有无', '能不能', '能够', '能不能够', '可不可以', '可不', '是吧', '是不是啊', '难道是', '应该', '大概', '大约', '可能', '或许', '恐怕', '大概是', '可能是', '或许是', '恐怕是', '咋回事儿', '都没有', '推荐', '医院', '机器人', '代跑', '废物', "鱼", "收", '抢不到', '糖分', '注意身体', '安全', '自动评价', '去广告', '去更新', '违约', '妈的', '起诉', '稳否', '咨询', '请教', '私聊', '交作业', '老赖', '代下', '血亏', '曝光', '骗', '骚扰', '禁止', '互助', '组队', '重复', '臭', '妹妹', 'TMD', 'tmd', 'Tmd', '泛滥', '没意思', '白眼狼', '搬砖', '狗', '炫耀', '休息', '睡觉', '大佬', '不薅', '也罢', '无语', '我服了', '今天生日', '生日快乐', '科教兴国', '🐟', '嘛', '出', '有空', '去玩', '？', '?','难绷','谁要','真的假的','有偿','多舒服','老哥们','真恶心','***','举报','闲得慌','跑路','太坑','避坑','被封','提个醒','好像','被','打击','借','敷衍','居然','修','咋','恶心','帮','操','么','救','好烦','打扰','谅解','终于','烟','医生','难受','睡','服了', "不如","牛马","工作","结婚", "辞职", "焦虑", "随波逐流", "捍卫", "精神", "追风", "读书", "苦逼", "打工", "你好", "小黑子", "鸡你太美", "测试", "鸡你太美了", "谁懂啊", "家人们", "小屁孩", "死", "拉屎", "对比", "好卡", "尘埃", "不服", "来辩", "离谱", "恐怖", "友善", "回马枪", "要命",]
regx_text= ['谁.*有']


#问卷调查域名
survey_domain = ['wjx',"wj.qq",'jiandaoyun','docs.google','formstack','typeform','zoho','mikecrm','jinshuju','fanqier','shenqingtong','wenjuan','51diaocha','weidiaocha','ebdan']



def check_word_in_text(text):
    # Create a copy of the word_list
    filtered_word_list = list(word_list)
    
    if 'http' in text:
        filtered_word_list.remove('?')
        
    escaped_words = [re.escape(word) for word in filtered_word_list]
    escaped_words+=regx_text+survey_domain
    pattern = '|'.join(escaped_words)
    regex = re.compile(pattern)
    match = regex.search(text)
    
    if match:
        print(f"匹配到关键词: {match.group()}")
        return False
    else:
        return True


def check_title_and_content(title, content):
    title_check = check_word_in_text(title)
    content_check = check_word_in_text(content)
    return title_check and content_check
