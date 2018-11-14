#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scrapy180803.spiders.lianjia import LianjiaSpider

__author__ = 'Terry'

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import redis

# 获取settings.py模块的设置
settings = get_project_settings()
process = CrawlerProcess(settings=settings)

# 可以添加多个spider类
process.crawl(LianjiaSpider)

# 启动爬虫，会阻塞，直到爬取完成
process.start()
