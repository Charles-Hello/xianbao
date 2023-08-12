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
        with FileLocker(file_path, 'r') as file:
            first_line = file.readline().strip()

        # 检查第一行内容是否是今天的日期
        if first_line != formatted_today:
            # 如果不是今天日期，则清空文件并写入今天日期
            with FileLocker(file_path, 'w') as file:
                file.write(formatted_today)
                previous_ids = []
                return previous_ids
        else:
            with FileLocker(file_path, 'r') as file:
              previous_ids = file.read().splitlines()
              return previous_ids

    except FileNotFoundError:
        # 如果文件不存在，则创建文件并将先前的id列表设置为空列表
        with FileLocker(file_path, 'w') as file:
            file.write(formatted_today)
            previous_ids = []
            return previous_ids
          




