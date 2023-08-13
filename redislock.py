import redis
from config import redishost,redisport
pool = redis.ConnectionPool(host=redishost, port=redisport, decode_responses=True)
r = redis.Redis(connection_pool=pool)
# 创建一个锁
num = "15"
def createlock(lockname):
    lock = r.lock(lockname+num) #创建一个锁
    r.expire(lockname+num) #设置锁的过期时间为30秒
    return lock
def check_lock_existence(lockname):
    if r.exists(lockname+num):
        return True
    else:
        return False

# try:
#     # 获取锁
#     lock =createlock("test3")
#     lockres = lock.acquire()
#     print(lockres)
#     # time.sleep(7)
# except Exception as e:
#     print(e)
# finally:
#     check_lock_existence("test3")
#     if c ==1:
#         lock.release()
#     else:
#         print("没有锁")
