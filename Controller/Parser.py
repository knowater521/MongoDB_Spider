# -*- coding: UTF-8 -*-
"""
Created on 2017年9月20日
@author: Leo
"""

from bs4 import BeautifulSoup
from Model.DownloadModel import *
from Utils.Convert import *
import urllib.request as ur
import time


class Parser:
    def __init__(self):
        self.soupWay = "html.parser"
        self.url = "https://www.mongodb.org/dl/"
        self.version = "win32/x86_64-2008plus-ssl"
        self.timeout_time = 10
        self.parser_tr = "tr"
        self.parser_td = "td"
        self.parser_a = "a"

        self.timeFormat = "%Y-%m-%d %H:%M:%S"

    def parser(self):
        # urllib解析页面
        html = ur.urlopen(self.url + self.version, timeout=self.timeout_time)

        # BeautifulSoup解析DOM标签
        soup = BeautifulSoup(html, self.soupWay)

        # 获取所有的tr标签
        trs = soup.find_all(name=self.parser_tr)

        file_list = []
        for tr in trs[1:]:
            each_mgo = EachVersion()
            tr_soup = BeautifulSoup(str(tr), self.soupWay)
            tds = tr_soup.find_all(name=self.parser_td)

            # 文件名和下载链接
            each_mgo.set_name(tds[0].get_text().replace("win32/mongodb-win32-x86_64-2008plus-ssl", "mongodb"))
            each_mgo.set_link(tds[0].find_all(name=self.parser_a)[0].get('href'))

            # 修改时间
            each_mgo.set_modified(str(int(time.mktime(time.strptime(tds[1].get_text(), self.timeFormat)))))

            # 文件大小
            each_mgo.set_size(str(convert_bytes(int(tds[2].get_text()))))

            # MD5
            each_mgo.set_md5(tds[3].find_all(name=self.parser_a)[0].get('href'))

            # sig
            sig_tag = tds[4].find_all(name=self.parser_a)
            if len(sig_tag) > 0:
                each_mgo.set_sig(sig_tag[0].get('href'))
            else:
                each_mgo.set_sig("")

            # SHA1
            sha1_tag = tds[5].find_all(name=self.parser_a)
            if len(sha1_tag) > 0:
                each_mgo.set_sha1(sha1_tag[0].get('href'))
            else:
                each_mgo.set_sha1("")

            # SHA256
            sha256_tag = tds[6].find_all(name=self.parser_a)
            if len(sha256_tag) > 0:
                each_mgo.set_sha256(sha256_tag[0].get('href'))
            else:
                each_mgo.set_sha256("")

            file_list.append(each_mgo)

        for i in file_list:
            print(i)