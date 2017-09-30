# -*- coding: UTF-8 -*-
"""
Created on 2017年9月22日
@author: Leo
"""

import urllib.request as ur
from lxml import etree


class MainPage:
    def __init__(self):
        self.mainPage_url = "https://www.mongodb.com/download-center#community"

    def parser(self):
        req = ur.urlopen(self.mainPage_url)
        result = req.read().decode("UTF-8")
        selector = etree.HTML(result)
        option_osx = selector.xpath('//select[@id="downloads-version-select"]/option/text()')
        for i in option_osx:
            print(i)


if __name__ == '__main__':
    m = MainPage()
    m.parser()
