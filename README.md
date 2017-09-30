# MongoDB官网下载链接爬虫
---
* 目录
    * [开发环境](#DevelopEnv)
    * [安装方式](#HowToInstall)
    * [功能](#Function)
    * [技术点](#TechPoints)
    * [未来开发目标](#Future)

---
<h3 id="DevelopEnv">开发环境</h3>
Python 版本：3.4.4（尽量不要使用python 3.5,因为lxml库的问题，需要用到etree）
Python库列表：

* lxml --- `3.8.0`
* pymongo --- `3.5.1`

---

<h3 id="HowToInstall">安装方式</h3>
```shell
    pip install lxml
    pip install pymongo
```
Ps:
* 需要配置MongoDB数据库,这一版本暂时没保存到文件中。（以后待扩展修改）
* 后期将使用sqlite3,这样较轻便使用


---
<h3 id="Function">功能</h3>
1、获取MongoDB官网的Windows,Linux,OSX的安装包
2、保存到MongoDB数据库中

---
<h3 id="TechPoints">技术点</h3>
1、没啥技术点就是很正常的解析页面,方便接入自己的自动化配置MongoDB脚本

---

<h3 id="Future">未来开发任务</h3>
1、细化功能，对下载版本进行细分，目前还停留在官网的划分规则
2、对数据库的选型应该有所兼容，考虑轻便不需要特殊配置的数据库

---