# -*- coding: UTF-8 -*-
"""
Created on 2017年9月30日
@author: Leo
"""

# 系统库
import json

# 第三方库
from pymongo import MongoClient


class Mgo(object):
    def __init__(self, collection_name):
        # 数据库基本配置
        self.mgo_conf = json.load(open("./conf/mgo.conf"))
        self.client = MongoClient(host=self.mgo_conf['address'], port=self.mgo_conf['port'])

        # 数据库名
        self.db = self.client[self.mgo_conf['database']]

        # 集合名
        self.collection_name = collection_name
        self.collection = self.db[self.collection_name]

    # 插入数据
    def insert_data(self, data):
        # 需要将Transfer对象用str强转后，在用eval方法转成字典，写入到MongoDB数据库
        try:
            self.collection.insert(eval(str(data)))
            return True
        except Exception as err:
            # 出错报错
            print(err)
            return False
