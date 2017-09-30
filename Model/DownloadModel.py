# -*- coding: UTF-8 -*-
"""
Created on 2017年9月20日
@author: Leo
"""


class EachVersion(object):
    def __init__(self):
        self.id = None  # id
        self.name = None  # 文件名
        self.link = None  # 下载链接
        self.modified = None  # 修改时间
        self.size = None  # 大小
        self.md5 = None  # MD5
        self.sig = None  # SIG签名
        self.sha1 = None  # SHA1
        self.sha256 = None  # SHA256

    # Getter Setter
    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_link(self):
        return self.name

    def set_link(self, value):
        self.link = value

    def get_modified(self):
        return self.modified

    def set_modified(self, value):
        self.modified = value

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def get_md5(self):
        return self.md5

    def set_md5(self, value):
        self.md5 = value

    def get_sig(self):
        return self.sig

    def set_sig(self, value):
        self.sig = value

    def get_sha1(self):
        return self.sha1

    def set_sha1(self, value):
        self.sha1 = value

    def get_sha256(self):
        return self.sha256

    def set_sha256(self, value):
        self.sha256 = value

    def __str__(self):
        return str({"_id": self.id,
                    "fileName:": self.name,
                    "downloadLink": self.link,
                    "size:": self.size,
                    "modified:": self.modified,
                    "md5:": self.md5,
                    "sig": self.sig,
                    "sha1": self.sha1,
                    "sha256": self.sha256})
