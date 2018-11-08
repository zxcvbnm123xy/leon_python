#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Leon'


import requests,re
headers={
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 7.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}
params={
    'admin': 'test',
    'passwd': '123'
}

url='http://slide.news.sina.com.cn/slide_1_86058_331364.html#p=1'
response=requests.get(url,params=params,headers=headers)
response.encoding = 'gbk'
content=response.text
# print(content)

title='<title>(.*?)_.*?</title>'
t=re.search(title,content,re.RegexFlag.M)
print(t.group(1))

description='<meta name="description" content="(.*?)" />'
d=re.search(description,content,re.RegexFlag.M)
print(d.group(1))