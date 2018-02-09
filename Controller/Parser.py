# -*- coding: UTF-8 -*-
"""
Created on 2017年9月20日
@author: Leo
"""

# 系统库
import time
import urllib.request as ur

# 第三方库
from bs4 import BeautifulSoup

# 项目库
from Model.DownloadModel import *
from Utils.Convert import *
from .mgo import Mgo


class Parser:
    def __init__(self, version):
        # BeautifulSoup方式
        self.soupWay = "html.parser"

        # 链接
        self.url = "https://www.mongodb.org/dl/"

        # 版本
        if version == "linux":
            self.version = version
            self.replace_string = "linux/mongodb-linux-x86_64"
        elif version == "windows":
            self.version = "win32/x86_64-2008plus-ssl"
            self.replace_string = "win32/x86_64-2008plus-ssl"
        elif version == "osx":
            self.version = version
            self.replace_string = "osx/mongodb-osx-ssl-x86_64"

        # 目标替换词
        self.replace_target_string = "mongodb"

        # 超时时间
        self.timeout_time = 10

        # 标签
        self.parser_tr = "tr"
        self.parser_td = "td"
        self.parser_a = "a"

        # 日期格式
        self.timeFormat = "%Y-%m-%d %H:%M:%S"

    def parser(self):
        # 开始爬虫
        print("Start parsing...")

        # urllib解析页面
        html = ur.urlopen(self.url + self.version, timeout=self.timeout_time)

        # BeautifulSoup解析DOM标签
        soup = BeautifulSoup(html, self.soupWay)

        # 获取所有的tr标签
        trs = soup.find_all(name=self.parser_tr)

        # 记录数
        count = 1

        # 写入数据库
        if self.version == self.replace_string:
            mgo = Mgo(collection_name="windows")
        else:
            mgo = Mgo(collection_name=self.version)

        # 核心逻辑
        for tr in trs[1:]:
            # 开始加载代码透析
            print("Get Data...")

            # 初始化实体类
            each_mgo = EachVersion()

            # tr标签
            tr_soup = BeautifulSoup(str(tr), self.soupWay)

            # 所有td标签
            tds = tr_soup.find_all(name=self.parser_td)

            # 文件名和下载链接
            each_mgo.set_name(tds[0].get_text().replace(self.replace_string, self.replace_target_string))
            each_mgo.set_link(tds[0].find_all(name=self.parser_a)[0].get('href'))

            # 修改时间
            each_mgo.set_modified(str(int(time.mktime(time.strptime(tds[1].get_text(), self.timeFormat)))))

            # 文件大小
            each_mgo.set_size(str(convert_bytes(int(tds[2].get_text()))))

            # MD5
            md5_tag = tds[3].find_all(name=self.parser_a)
            if len(md5_tag) > 0:
                each_mgo.set_md5(md5_tag[0].get('href'))
            else:
                each_mgo.set_md5("")

            # SIG签名
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

            # 最后set_id
            each_mgo.set_id(md5_constructor(str(each_mgo.get_link())))

            # 插入数据
            if mgo.insert_data(each_mgo):
                # 输出完成记录数
                print("已完成 %d 条" % count)
                count += 1
            else:
                print("出错了!...")
                return

