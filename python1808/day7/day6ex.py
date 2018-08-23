# 1.给定一个字符串，要求删除字符串中的重复元素。
# 序列
# 思路，拿到字符串中的每一个元素，
# 新创建一个字符串，
# 跟原有字符串中的所有元素比较，
# 如果当前字符串在新字符串中存在，则不加入，如果不存在则加入
s="didudfjdklfjdfjdfjkjjj"
s_new=""
for i in s:
    if i not in s_new:
        s_new+=i
print(s_new)




# 2、使用数值类型、布尔类型、字符串、字节，
# 分别使用不同的变量指向相同的内容，以及不同的变量绑定已有变量，
# 验证以上数据类型的is和==运算。
i1=1
i2=1
i3=i1
print(i1==i2)
print(i1==i3)
print(i2==i3)
print(id(i1),id(i2),id(i3))

i1="abc"
i2="abc"
i3=i1
print(id(i1),id(i2),id(i3))


i1=b"abc"
i2=b"abc"
i3=i1
print(id(i1),id(i2),id(i3))


i1=True
i2=True
i3=i1
print(id(i1),id(i2),id(i3))

c=1<3
print(id(c),id(i1))


# 3. 判断输入的一个数是不是质数
# import math
# num=input("输入一个数")
# if num.isnumeric():
#     num=int(num)
#     tag=True
#     for i in range(2,int(math.sqrt(num))+1):
#         if num%i==0:
#             print("不是质数")
#             tag=False
#             break
#     if tag:
#         print("是质数")
# else:
#     print("您输入的不是一个数字")

# 4.输出100以内所有的质数
# for j in range(2,101):
#     tag=True
#     for i in range(2,int(math.sqrt(j))+1):
#         if j%i==0:
#             # print("不是质数")
#             tag=False
#             break
#     if tag:
#         # print("是质数")
#         print(j)


# 5.完成路径的组装，先提示用户多次输入路径，当输入exit时，
# 输出完整路径，如/home/python/ftp/share
# path=""
# for i in range(100):
#     t=input("请输入一个路径：")
#     if t=="exit":
#         break
#     else:
#         path+="/"+t
# print(path)

# 6. 根据输入的1,2，3 确定中午吃什么 。1 牛肉面   2 红烧肉盖饭  3 吃土
# 可以使用random模块的randint函数随机产生（1,2,3）。
# 使用时先导入random模块。Randint（a,b）：可以产生一个x ，a<=x<=b
import random
# n=random.randint(1,3)
# if n==1:
#     print("牛肉面")
# else:
#     if n==2:
#         print("红烧肉")
#     else:
#         print("吃土")


# 7. 改进入门游戏，realvalue使用random产生，如果猜错了，
# 则可以提示猜大了，还是猜小了。
realvalue=random.randint(1,10)
c=3
for i in range(3):
    guess=input("请输入我心里的数字：")
    if guess.isnumeric():
        guess=int(guess)
        if guess==realvalue:
            print("猜对了")
            break
        else:
            c-=1
            print("猜错了")
            if guess>realvalue:
                print("猜大了，小一点")
            else:
                print("猜小了，大一点")
    else:
        print("输入有误")
if c==0:
    print("小笨蛋，3次都没猜出来")