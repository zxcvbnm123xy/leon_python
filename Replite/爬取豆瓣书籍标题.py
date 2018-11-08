#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'leon'

import requests,re


url='https://book.douban.com/'
headers={
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 7.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'Accept': '*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

response = requests.get(url,headers=headers)
content=response.text
# print(content)

title_r = '<a class="" href=".*?" title="(.*?)">'
title= re.findall(title_r, content,re.RegexFlag.S|re.RegexFlag.M)
for i in title:
    print(i)
#运行结果：只出来第一本书的标题  命运晚餐
