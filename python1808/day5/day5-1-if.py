"""
第五章：流程控制
所谓的流程控制就是程序执行的过程
三种结果：
顺序执行：按部就班
选择：根据条件不同执行不同的代码段
循环：体现的是重复性的执行一件事
"""
# 缩进：python使用每行前面的空白（缩进）来决定当前代码的层次。
"""
同一个层次的语句必须要有相同的缩进
通常情况下使用四个空格（tabs）来表示一个缩进层次
"""

# 一、选择判断
# 背景，有的时候希望程序是根据条件来按照不同的条件执行不同的代码，而不是按部就班的一行
#       一行执行。
# 所有的关键字
import keyword
print(keyword.kwlist)
# 1. if条件：当if条件成立的时候，会执行的代码段
"""
语法结构
if 条件（布尔类型）:
    当条件返回True，会执行的代码段
    当条件返回True，会执行的代码段
    当条件返回True，会执行的代码段
    ....
else:(else的后面没有条件)    
    当if条件返回False，会执行的代码段
    当if条件返回False，会执行的代码段
    当if条件返回False，会执行的代码段
其他代码段

用法注意：
（1）if可以单独存在，但是else不可以
（2）if后面有条件，else后面没有条件
"""
a=101
if a<=100:
    print("我现在很瘦")
    print("我可以继续胡吃海塞")
else:
    print("我不能吃饭了")
    print("还得去减肥")
print("其他的代码段")

# 练习：
# 1. 输入一个成绩，如果>=60就输出及格了，否则输出:这次得交挂科费了，回家还不能吃饭。
# score=int(input("请输入你的成绩"))
# if score>=60:
#     print("及格了")
# else:
#     print("交挂科费")
#     print("回家不能吃饭")

# 2.根据今天是星期几（1-7），输入星期几，输出要做的事情：
# 周一-周五 上课
# 周六      自习
# 周日      休息
# day=int(input("请输入星期几："))
# if day==6:
#     print("自习")
# if day==7:
#     print("休息")
# if 1<=day<=5:
#     print("上课")

#问题：
# 1. 效率，当条件符合了一个if之后，还会走其他的if条件
# 2. 如果输入的8

# 解决：
# 1.使用嵌套if来解决多次执行if问题
# 2.将概率大的放在前面

# 小知识：debug
# 1. 设置断点：当使用debug模式执行的时候，代码就会停止在断点的位置
# 2. F8键，会使程序一行 一行执行
# 3. F9键，能够使得程序走完（走到下一个断点）
# 4. 鼠标悬停在变量的位置，会显示变量值

"""
if 布尔条件：
   if 布尔条件：
      语句体
   else:
      语句体
else:
   if 布尔条件：
      语句体
   else:
      语句体
"""

# day=int(input("请输入星期几："))
# if 5>=day>=1:
#     print("上课")
# else:
#     if day==6:
#         print("自习")
#     else:
#         if day==7:
#             print("休息")
#         else:
#             print("输入错误")


# 3. 输入一个工资，如果工资<=5000，输出我很穷；
# 如果<=10000，输出可以温饱；如果<=20000,输出我是土豪
salary=int(input("请输入一个工资："))
if salary<=5000:
    print("我很穷")
else:
    if salary<=10000:
        print("可以温饱")
    else:
        if salary<=20000:
            print("我是土豪")

# if salary<=5000:
#     print("我很穷")
# else:
#     if 10000<=salary<=20000:
#         print("我是土豪")
#     else:
#         print("可以温饱")
