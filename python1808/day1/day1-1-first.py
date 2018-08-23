"""
第一章 python的入门

语言：人和人之间的沟通
计算机的语言：人和计算机之间沟通的语言


计算机语言按照语言的级别：
机器语言：计算机只能识别机器语言 0  1
汇编语言：助记符 指令 add 2 3 goto
高级语言：python    c语言    c++   .net    java    php ,越高级的语言越贴近人

计算机语言执行的方式：
（1）编译执行
（2）解释执行：python就是解释型的语言
     优点：移植性
     缺点：执行的速度比较慢，因为每执行一次，就要使用解释器进行一次解析。
"""

# 一、 python的介绍
# 1. python的发展史
"""
荷兰人  龟叔 
开发过一门教学语言ABC，因为语言本身不开放
1989年圣诞节 励志开发python，开源 
名字由来：飞行的马戏团 蟒蛇

为什么人工智能的开发选择了python？
facebook  2017 科学计算的工具torch， 针对python开发了pytorch、
python的在人工智能领域的霸主地位就被决定

"""

# 2.python版本
# 我们使用3.6作为教学 版
# 3.6.5
# python中主要分为两个版本
# 2x版本，官方发布到2.7。
# 3x版本，一直向后发展 产生完全是为摒弃python2版本中的问题。
# 40%  3
# 60%  2

# 3.python的特点
# 世界上最好的编程语言，没有，各有各的特点
# （1）语法简洁
# （2）既可以面向过程也可以面向对象
# （3）解释执行，跨平台
# （4）可扩展性
# （5）具有强的大的支持库

# 缺点：
# （1）执行速度慢  java  c 0.01s     0.1s    1s   1.01s  1.1s
# （2）无法加密

# 4.python的应用领域
# （1）web应用开发
# （2）网络爬虫
# （3）数学分析和科学计算
# （4）人工智能
# （5）游戏开发


# 二、python的开发环境
# 1.python3.6
# 注意：一定要勾选add path，注意建议安装到自定义的文件夹。
# 2.pycharm
# 安装 ，注意建议安装到自定义的文件夹，注意勾选已存在的解析器（已安装的python.exe）
# （暂时不要新创建虚拟环境venv）


# 三、第一个python程序
# python程序的执行
# 1.交互式执行
#  先找到控制台，在控制台中输入python命令（相当于调用python的解释器）
#  输入python代码
# 一句一句执行

# 2.脚本式执行
# 脚本:python的脚本  .py文件
# （1）在控制台中进入到脚本文件所在的目录下
# （2）输入python命令+ 文件.扩展名

print("hello world1")
print("hello world2")
print("hello world3")
print("hello world4")
print("hello world5")