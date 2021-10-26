# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 14:22
# @Author  : kif
# @FileName: createToken.py
# @Software: PyCharm

import datetime
import jwt

SALT = 'J4+opkLMck%W5pC3~^@YRGDmR&Du&E~9ObDVt$p)psyk#v'

def creattoken(user_data):
    # 构造header
    headers = {
        'typ': 'jwt',
        'alg': 'HS256'
    }
    # 构造payload
    payload = {
        'id': user_data.id,
        'email': user_data.userEmail,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=720)  # 超时时间
    }
    return jwt.encode(payload=payload, key=SALT, algorithm="HS256", headers=headers).encode('utf-8').decode(
        "utf-8")
