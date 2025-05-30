from enum import Enum


class ResponseMessage(Enum):
    SUCCESS = "成功"
    ERROR = "失败"


class LoginResponseMessage(Enum):
    """
    登录返回信息枚举
    """
    PASSWORD_ERROR = "账号或密码错误"
