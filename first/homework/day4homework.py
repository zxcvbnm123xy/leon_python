#1.输出如下内容：分别使用双引号，和三引号。
#双引号
def que():
    s = "A：are you \"tom\""
    s1 = "B:no"
    print(s)
    print(s1)

    #三引号
    c = """
    A:are you "tom"
    B:no
    """
    print(c)

    #2.定义两个字符串，a=“hello”  b=”hello”，令c=a，思考：是否能对a中的h进行修改
    #输出abc三个变量的值
    #使用is和==判断abc之间的关系，并画出内存图
    a = "hello"
    b = "hello"
    c = a
    a = a.replace("h", "y")
    print(a +"," +  b + "," + c)
    print(a is b)
    print(c is a)
    print(c is b)
    #print(a == b)
    #print(a == c)
    #print(c == b)

    #3.分别输入3个爱好，打印出来“我的爱好是**、**、**” ，使用格式化输出
    h1 = "python"
    h2 = "编程"
    h3 = "人工智能"
    print("我的爱好是：%s,%s,%s" %(h1 , h2 , h3))

    #4.这是一个地址，http://news.gzcc.cn/html/2017/xiaoyuanxinwen_1027/8443.html
    #其中1027/8443是新闻编号，想办法获得新闻编号。至少两种方法。

    #第一种方法
    str  = "http://news.gzcc.cn/html/2017/xiaoyuanxinwen_1027/8443.html"
    print('采用定位方法：', str[-14:-5])

    #第二种方法
    str  = "http://news.gzcc.cn/html/2017/xiaoyuanxinwen_1027/8443.html"
    c = str.split('_')
    c = c[1].split(".")
    print('用split方法：', c[0])

#5.做如下练习：
# 1.输入一种水果，如葡萄
# 2.打印类似“吃葡萄不吐葡萄皮，不吃葡萄倒吐葡萄皮”的效果
# 3.使用切片，切出自己输入的水果
# 4.使用strip，剪切到自己输入的水果
# 5.统计打印的的文本中，水果出现的次数
def que():
    fruit="火龙果"
    s="吃{}不吐{}皮，不吃{}倒吐{}皮".format(fruit,fruit,fruit,fruit)
    print(s)
    print(s[1:len(fruit)+1])
    #吃火龙果不吐火龙果皮，不吃火龙果倒吐火龙果皮
    print(s.strip("吃皮不吐"+fruit).strip("，不吃倒"))
    print(s.count(fruit))

#练习，输入一个成绩，如果>=60就输出及格了，否则输出，这次得交挂科费了，回家还不能吃饭
def que():
    score = input("请输入你的成绩：")
    if eval(score) >= 60:
        print("及格了！")
    else:
        print("这次得交挂科费了，回家不能吃饭")

#练习2，根据今天是星期几（1-7），输入星期几，输出要做的事。
#周一-周五，上课
#周六       自习
#周日       休息
def que1():
    date = int(input("请输入今天周几："))
    if date <= 7:
        if 1 <= date <= 5:
            print("今天上课！")
        else:
            if date == 6:
                print("今天放假！")
            else:
                if date ==7:
                    print("今天自习！")
    else:
        print("输入错误！")

    #3.输入一个工资，如果工资<= 5k，输出我很穷，如果<= 10k,输出可以温饱；如果<=20k,输出我是土豪
    salary=int(input("请输入一个工资："))
    if salary<=5000:
        print("我很穷")
    else:
        if salary<=10000:
            print("可以温饱")
        else:
            if salary<=20000:
                print("我是土豪")

#练习，
"""
1.定义字符串，定义字节，使用for循环对其进行遍历，计算长度
2.输出1-100以内的所有奇数，使用两种方法
3.输出1-100以内的所有偶数
4.有一些温度 30,50，66,99,20,58代表华氏温度，希望将这些温度变成摄氏温度：摄氏温度=（华氏温度-32）/1.8
"""

def que():
    #定义字符串，定义字节，使用for循环对其进行遍历，计算长度
    str = "askjdlka"
    for i in str:
        print(i)
    print(len(str))

    #定义字符串，定义字节，使用for循环对其进行遍历，计算长度
    b = b"sadasdas"
    l = 0
    for i in b:
        print(i)
        l += 1
    print(l)

    #s输出奇数
    a = range(1, 101)
    for i in a:
       if i % 2 == 1:
        print(i, end = "\t" )

    for i in range(1, 101, 2):
        print(i)

    #输出偶数
    a1 = range(1, 101)
    for i in a1:
       if i % 2 == 0:
        print(i, end = " " )

    for i in range(2, 101, 2):
        print(i)

#4.有一些温度 30,50，66,99,20,58代表华氏温度，希望将这些温度变成摄氏温度：
# 摄氏温度=（华氏温度-32）/1.8
#(1)需要将每个温度变成摄氏温度
#（2）希望得到的结果仍然是字符串
"""
思路：
（1） 如何将字符串处理成单个元素；split(",")
（2）使用for循环，处理每一个温度，
    处理之前需要将温度转成float
（3）+可以拼接字符串，format也能组装字符串
"""
def que():
    s = "30,50，66,99,20,58"
    print(s.split(","))
    t = s.split(",")
    a = ""
    for i in t:
        print(i)
        x=(float(i) - 32)%1.8
        print(x)
        # a += str(x) + ","
        a += "{}," .format(x)
    s = a.strip(",")
    print(s)

#输入一个数，判断是不是质数
s = int(input("请输入一个数："))
for i in range(2, s):
    if s%i == 0:
        print("不是质数！")
        break
    else:
        if i == s-1:
            print("是质数！")
