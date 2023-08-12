import redis
from config import redishost,redisport
pool = redis.ConnectionPool(host=redishost, port=redisport, decode_responses=True)
r = redis.Redis(connection_pool=pool)
# 创建一个锁
def createlock(lockname):
    lock = r.lock(lockname+"4") #创建一个锁
    # r.expire(lockname) #设置锁的过期时间为30秒
    return lock
# try:
#     # 获取锁
#     lockres = lock.acquire()
#     print(lockres)
#     time.sleep(7)
# except Exception as e:
#     print(e)
# finally:
#     lock.release()
