import redis
from config import redishost,redisport
pool = redis.ConnectionPool(host=redishost, port=redisport, decode_responses=True)
r = redis.Redis(connection_pool=pool)


# 创建一个锁
keyname = 'mylock'
lock = r.lock(keyname) #创建一个锁
r.expire(keyname, 30) #设置锁的过期时间为30秒
# try:
#     # 获取锁
#     lockres = lock.acquire()
#     print(lockres)
#     time.sleep(1)
# except Exception as e:
#     print(e)
# finally:
#     lock.release()
