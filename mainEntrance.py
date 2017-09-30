# -*- coding: UTF-8 -*-
"""
Created on 2017年9月20日
@author: Leo
"""

from Controller.Parser import *


if __name__ == '__main__':
    version = ""
    print("选择你的版本: (1、Windows(仅支持64位 & 有SSL插件). 2、Linux. 3、Mac OSX(仅支持有SSL插件) )")
    print("Choose your version: (1、Windows(only 64bits & with SSL). 2、Linux. 3、Mac OSX(with SSL) )")
    choice = input()
    if choice == "1":
        version = "windows"
        print("您选择的是 %s ." % version)
    elif choice == "2":
        version = "linux"
        print("您选择的是 %s ." % version)
    elif choice == "3":
        version = "osx"
        print("您选择的是 %s ." % version)
    else:
        raise ValueError("Illegal Choice you input!")

    parser = Parser(version=version)
    parser.parser()

