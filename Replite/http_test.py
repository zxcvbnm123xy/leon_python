#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Leon'

import requests
import urllib3

r=requests.get("http://www.baidu.com")

r.encoding=("utf-8")

print(r.text)