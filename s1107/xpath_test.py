#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Terry'



html_doc = '''
<html>
  <head>
   <title>
    The Dormouse's story
   </title>
  </head>
  <body>
   <p class="title">
    <b>
     The Dormouse's story
    </b>
   </p>
   <p class="story">
    Once upon a time there were three little sisters; and their names were
    <a class="sister" href="http://example.com/elsie" id="link1">
     Elsie
    </a>
    <a class='test_a'>test_text</a>
    and
    <a class="sister" href="http://example.com/tillie" id="link2">
     Tillie
    </a>
    and they lived at the bottom of a well.
   </p>
   <p class="story">
    测试中文
   </p>
  </body>
</html>
'''

# 导入 etree
from lxml import etree

# 爬虫使用最常用的是这个HTML加载方式
# tree = etree.HTML(html_doc) # 会自动补全 html 标签
# print(etree.tostring(tree, encoding="utf-8").decode('utf-8'))  # 打印输出查看效果

# # 和HTML差不多，但是不会补全html标签
# tree = etree.fromstring(html_doc)
# print(etree.tostring(tree, encoding="utf-8").decode('utf-8'))  # 打印输出查看效果

# # 用于加载这个xml文件
# tree = etree.XML(html_doc)
# print(etree.tostring(tree, encoding="utf-8").decode('utf-8')) # 打印输出查看效果


#加载内容
tree = etree.HTML(html_doc)

print(tree.xpath('//title')[0].text) # 节点内容 , 推荐使用这种方式
print(tree.xpath('//title/text()')[0]) # 节点内容
#
# print(tree.xpath('//title')[0].tag)  # 节点名
# print(tree.xpath('//p[@class="story"]')[1].text)
#
# print(etree.tostring(tree.xpath('//title')[0]))  # etree.tostring 输出节点全部信息 是bytes类型，包含了节点本身
#
# print(tree.xpath('//title')[0].getparent().tag)  # 父节点
#
# print(tree.xpath('//a')[1].get('class'))  # 获取属性
# print(tree.xpath('//a')[1].attrib)  # 所有属性的字典
#
# print(tree.xpath("//text()")) # 所有字符串，列表形式
# print(tree.xpath("//text()")[2]) # 所有字符串，列表形式
#
# print(tree.xpath("string()")) # 所有文本，字符串 类型，以单一标签为分界，如 <br/>
#
# # 多属性
# print(tree.xpath('//a[@class="sister" and @id="link2"]')[0].text)
#
# print(tree.xpath('//a[@class="sister" and contains(text(), "Tillie")]')[0].text) # contains 包含属性
#
# print(tree.xpath('//a[@class="sister" and text()="Tillie"]')[0].text) # 文本text() 等于某个值