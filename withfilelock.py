
from redislock import createlock,check_lock_existence
import portalocker
class FileLocker:
    def __init__(self, filename, mode, **file_open_kwargs):
        self.filename = filename
        self._mode = mode
        self._file_open_kwargs = file_open_kwargs
        self._flags = portalocker.LOCK_EX
        self._file = None

    def __enter__(self):
        self._file = open(self.filename, self._mode, **self._file_open_kwargs)
        portalocker.lock(self._file, flags=self._flags)
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        portalocker.unlock(self._file)
        self._file.close()

from datetime import datetime
# 获取今天的日期
today_date = datetime.now().date()
formatted_today = today_date.strftime('%Y-%m-%d')

def file_previous_ids(file_path):
    try:
        
    # 打开文件，获取第一行内容
        with open(file_path, 'r') as file:
            first_line = file.readline().strip()

        # 检查第一行内容是否是今天的日期
        if first_line != formatted_today:
            # 如果不是今天日期，则清空文件并写入今天日期
            with open(file_path, 'w') as file:
                file.write(formatted_today)
                previous_ids = []
                return previous_ids
        else:
            #上一个进程还没来得及修改文本内容，这个进程就已经读取了，所以会出现错误
            #这里检查是否有加锁的行为，如果有则等待才能进行
            lock = createlock(file_path)
            lockresstatus = lock.acquire()
            
            #todo:
            # print(f"{file_path}锁状态:")
            # print(lockresstatus)
            
            
            print(f'{file_path}拿到锁钥匙')
            with open(file_path, 'r') as file:
                previous_ids = file.read().splitlines()
                #这里读取完毕。加锁
                return previous_ids,lock
            
          
    except FileNotFoundError:
        # 如果文件不存在，则创建文件并将先前的id列表设置为空列表
        with open(file_path, 'w') as file:
            file.write(formatted_today)
            previous_ids = []
            return previous_ids,None
          
def write_current_ids(file_path, current_ids,lock):
    with open(file_path, 'a+') as file:
        current_ids_str = [str(item) for item in current_ids]
        file.write('\n'+'\n'.join(current_ids_str))
        if lock:
            res = check_lock_existence(file_path)
            if res:
                lock.release()
                print(f'{file_path}正常解开锁钥匙')


