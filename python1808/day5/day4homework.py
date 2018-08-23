# 1.
# 输出如下内容：分别使用双引号，和三引号
# A：are you "tom"
# B：no
def que1():
    a="hello"
    "hello"  # 匿名字符串 也创建的内存，只不过没有名字，用起来不太方便
    print("A：are you \"tom\"\nB：no")

    print("""
    A：are you "tom"
    B：no
    """)

# a="helloworld".replace("o","*")
# print(a)
# b=print(a.count("h"))
# print(b)

#
# 2.定义两个字符串，a =“hello”  b =”hello”，令c = a，
# 思考：是否能对a中的h进行修改
# 输出abc三个变量的值
# 使用is和 == 判断abc之间的关系，并画出内存图
def que2():
    a="hello"
    b="hello"
    c=a
    print(id(a),"a原始id")
    # a[0]="6"  #字符串的元素不能被修改，字符串属于 不可变类型（数值、布尔、字节、字符串）
    a="6"+a[1:]
    print(id(a),"a变化之后的id")
    print(a,b,c)
    print(a==c)
    print(b==c)
    print(b==a)
    print(a is b)
    print(c is b)
    print(c is a)





#
# 3.
# 分别输入3个爱好，打印出来“我的爱好是 **、 ** 、 ** ” ，使用格式化输出
def que3():
    h1=input("请输入第一个爱好：")
    h2=input("请输入第二个爱好：")
    h3=input("请输入第三个爱好：")
    # print("我的爱好是%s,%s,%s" % (h1,h2,h3))
    print("我的爱好是{},{},{}".format(h1,h2,h3))
    print(f"我的爱好是{h1},{h2},{h3}")
# h=input("请输入你的爱好")
# print("我的爱好是{}".format(h))
#
# 4.
# 这是一个地址，http: // news.gzcc.cn / html / 2017 / xiaoyuanxinwen_1027 / 8443. html
# 其中1027 / 8443
# 是新闻编号，想办法获得新闻编号。至少两种方法。
def que4():
    # 去掉内部的空格
    s="http: // news.gzcc.cn / html / 2017 / xiaoyuanxinwen_1027 / 8443. html"
    # http://news.gzcc.cn/html/2017/xiaoyuanxinwen_1027/8443.html
    print(s.replace(" ",""))
    s=s.replace(" ","")
    # 方式一：切片
    print(s[-14:-5])
    # 方式二：切片+index
    print(s[s.index("_")+1:s.index(".html")])
    # 方式三：
    print(s.strip("http://news.gzcc.cn/html/")[-9:])
    # 方式四：
    print(s.split("_")[1].rstrip(".html"))

#
#
# 5.
# 做如下练习：
# # 1.输入一种水果，如葡萄
# # 2.打印类似“吃葡萄不吐葡萄皮，不吃葡萄倒吐葡萄皮”的效果
# # 3.使用切片，切出自己输入的水果
# # 4.使用strip，剪切到自己输入的水果
# # 5.统计打印的的文本中，水果出现的次数
fruit="火龙果"
s="吃{}不吐{}皮，不吃{}倒吐{}皮".format(fruit,fruit,fruit,fruit)
print(s)
print(s[1:len(fruit)+1])
#吃火龙果不吐火龙果皮，不吃火龙果倒吐火龙果皮
print(s.strip("吃皮不吐"+fruit).strip("，不吃倒"))
print(s.count(fruit))

