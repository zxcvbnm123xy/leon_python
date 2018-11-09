#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Leon'

from selenium import webdriver

driver=webdriver.Chrome()

driver.set_page_load_timeout(10)
# 设置10s脚本超时时间
driver.set_script_timeout(10)
driver.set_window_size(1366,768)


driver.quit()