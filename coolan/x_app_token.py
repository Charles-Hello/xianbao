import hashlib
import base64
import time


# 示例调用
device_id = "34de7eef-8400-3300-8922-a1a34e7b9b4f"

def md5(data):
    return hashlib.md5(data.encode()).hexdigest()

def generate_token():
    ctime = int(time.time())
    md5_timestamp = md5(str(ctime))
    arg1 = f"token://com.coolapk.market/c67ef5943784d09750dcfbb31020f0ab?{md5_timestamp}${device_id}&com.coolapk.market"
    md5_str = md5(base64.b64encode(arg1.encode()).decode())
    token = md5_str + device_id + "0x" + format(ctime, 'x')
    return str(token)


# token = generate_token(device_id)
