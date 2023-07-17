

from typing import Optional
from config import SYSTEM_PROXY


def get_local_proxy() -> Optional[str]:
    """
    说明:
        获取 config.py 中设置的代理
    """
    return SYSTEM_PROXY or None