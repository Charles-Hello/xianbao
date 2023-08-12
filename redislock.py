import redis
from config import redishost,redisport
pool = redis.ConnectionPool(host=redishost, port=redisport, decode_responses=True)
r = redis.Redis(connection_pool=pool)
import time 

# 创建一个锁
keyname = 'mylock4'
lock = r.lock(keyname) #创建一个锁
r.expire(keyname, 20) #设置锁的过期时间为30秒
# try:
#     # 获取锁
#     lockres = lock.acquire()
#     print(lockres)
#     time.sleep(7)
# except Exception as e:
#     print(e)
# finally:
#     lock.release()
