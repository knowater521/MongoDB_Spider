# -*- coding: UTF-8 -*-
"""
Created on 2017年9月20日
@author: Leo
"""

from bs4 import BeautifulSoup
from Model.DownloadModel import *
import urllib.request as ur

# url = "https://www.mongodb.org/dl/win32/x86_64-2008plus-ssl"
# req = ur.urlopen(url)
# result = req.read().decode("UTF-8")
# print(result)

from Controller.Parser import *


if __name__ == '__main__':
    parser = Parser()
    parser.parser()

