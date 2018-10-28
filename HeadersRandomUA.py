# -*- coding: utf-8 -*-
"""
创建时间：Sun Aug  5 09:42:55 2018
作者: 星空飘飘
平台：Anaconda 3-5.1.0
语言版本：Python 3.6.4
编辑器：Spyder
分析器：Pandas: 0.22.0
解析器：lxml: 4.1.1
数据库：MongoDB 2.6.12
程序名：headers随机UA.py
"""
import requests
from fake_useragent import UserAgent  # 获取headers中User-Agent 安装pip install fake_useragent

url = 'http://2018.ip138.com/ic.asp'
ua = UserAgent()  # 随机 User-Agent
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           'Host': '2018.ip138.com'
           }
headers['User-Agent'] = ua.random  # 随机生产模拟浏览器
response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding  # 识别编码
html = response.text
print(html)
