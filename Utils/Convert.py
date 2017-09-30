# -*- coding: utf-8 -*-
"""
Created on 2017年9月20日
@author: Leo
"""

# 系统库
import math
import hashlib


# 智能转换 bytes 为 kb/mb/gb/tb/pb...
def convert_bytes(size, lst=None):
    if lst is None:
        lst = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = int(math.floor(math.log(size, 1024)))

    if i >= len(lst):
        i = len(lst) - 1
    return ('%.2f' + lst[i]) % (size/math.pow(1024, i))


# MD5加密
def md5_constructor(string):
    md5 = hashlib.md5(string.encode('UTF-8')).hexdigest()
    return md5
