#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""智能转换 bytes 为 kb/mb/gb/tb/pb...
"""

import math


def convert_bytes(size, lst=None):
    if lst is None:
        lst = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = int(math.floor(math.log(size, 1024)))

    if i >= len(lst):
        i = len(lst) - 1
    return ('%.2f' + lst[i]) % (size/math.pow(1024, i))


def main():
    print(convert_bytes(84253081))


if __name__ == '__main__':
    # main()
    list_a = []
    print(len(list_a))
