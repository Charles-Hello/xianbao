



from typing import Optional


#代理，例如 "http://127.0.0.1:7890"
# 如果是WLS 可以 f"http://{hostip}:7890" 使用寄主机的代理
SYSTEM_PROXY: Optional[str] = None  # 全局代理

#push推送相关配置
dormitory = '12361142051@chatroom'
tnanko = 'wxid_xq2w7jl6cbi811'
jd_xianbao = '5748551094@chatroom'
jd_miaomiaomiao = "19244435890@chatroom"
group_id = '24446492186@chatroom'
user_id = 'wxid_p8geau233z3412'
taobao_fuli = '17573440617@chatroom'
taobao_xianbao = '5739151628@chatroom'
test_room = "19378256744@chatroom"  #我推送的线报群
Redis_ip = '192.168.1.155'  ## Redis地址
Redis_port = '19736'  ## Redis端口，默认为6379
Redis_pass = ''  ## Redis密码，无则不填
# 主动调用发送接口
# API_URL = "http://192.168.1.51:8090"
API_URL = "http://192.168.1.32:8000"
# 赚客先前的id列表文件路径
zhuanPrevious_ids_file = 'zhuankeprevious_ids.txt'


# 小嘀咕先前的id列表文件路径
XiaodiguPrevious_ids_file = 'XiaodiguPrevious_ids_file.txt'

#酷安先前的id列表文件路径
kuanPrevious_ids_file = 'kuanPrevious_ids_file.txt'


#原酷安
kuandiguPrevious_titles_file = 'kuandiguPrevious_titles_file.txt'

#原小嘀咕
XiaodiguPrevious_titles_file = 'XiaodiguPrevious_titles_file.txt'


#线报屋
xianbaowuPrevious_titles_file = 'xianbaowuPrevious_titles_file.txt'



#中转防红
transferurl= "https://charles-hello.github.io/qq_fanghong/api/?url="


#redis原生锁
redishost='192.168.1.155'
redisport=19736
