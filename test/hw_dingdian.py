#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Leon'

from bs4 import BeautifulSoup
from common import requests_helper
from lxml import etree
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()

class DingdianInfo:
    def __init__(self):
        self.session=requests_helper.make_session()

    def visit_page(self):
        url='https://www.23us.so/xiaoshuo/13332.html'

        response=self.session.get(url)
        response.encoding='utf-8'
        text=response.text
        self.tree=etree.HTML(text)
        self.soup=BeautifulSoup(text, 'lxml')
        # print(self.tree.xpath('//title')[0].text)

if __name__ == '__main__':
    dd=DingdianInfo()
    dd.visit_page()
    print("soup方式：")
    soup=dd.soup
    table_ele=soup.find('table',id='at')
    print("小说名：",soup.h1.text)
    print("小说类别：", table_ele.find_all('td')[0].text)
    print("作者：", table_ele.find_all('td')[1].text)
    print("状态：", table_ele.find_all('td')[2].text)
    print("全文长度：", table_ele.find_all('td')[4].text)
    print("总点击数：", table_ele.find_all('td')[6].text)

    print("xpath方式：")
    tree=dd.tree
    table_ele2=tree.xpath('//table')[0]
    print("小说名：", tree.xpath('//h1')[0].text)
    print("小说类别：",tree.xpath('//a[contains(@href,"/list/1_1.html")]')[0].text)
    print("作者：", table_ele2.xpath('//td[2]')[0].text)
    print("状态：", table_ele2.xpath('//td[3]')[0].text)
    # print("全文长度：", table_ele2.xpath('//td[4]')[0].text)
    # print("总点击数：", table_ele2.xpath('//td[7]')[0].text)

