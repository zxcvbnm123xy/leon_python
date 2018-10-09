"""
第十一章 模块和包
"""
# 二、包
# 1. 包的概念
# 包的概念：包提供了独立的命名空间有，类似于window系统中的文件夹。
# 注意：跟文件夹不同的是，python开发包必须要有__init__.py
#       普通的文件夹不能被导入，但是包可以被导入

# 2.包的使用
# 两种导入方式
# import 包名
# import 包名.模块名

# from 包名 import  模块名
# from 包名.模块命名 import 变量名，函数名。。。
# import day12.another1808
# from day12.another1808 import x,fun
# print(x)
# fun()

# 3.__init__.py
# python的每一个开发包下，都必须要init文件：用途是用来初始化的。
# 当import [包] 的时候，会执行当前包中__init__.py中的所有代码。
# __init__中一般都使用来初始化包中的变量。
# __init__.py文件中定义的变量或者函数或者类等等，一些列的名字，在整个包的所有py文件中都可以访问到
# import day12
# from day12 import another1808
# import day12
# 在py文件中访问当前包中的init文件，语法：
# 【包名】.属性名
# print(day12.x) # 使用import的形式访问

# 4. __all__变量
# all是一个列表，可以在列表下加入可以导入的名字
from  day12 import *
print(x)
print(y)

