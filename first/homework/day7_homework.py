# 1.遍历元素
L=[['Apple', 'Google', 'Microsoft'],
   ['Java', 'Python', 'Ruby', 'PHP'],['Adam', 'Bart', 'Lisa']]
def q1():
    for i in L:
        for j in i:
            print(j)


# 2.将数组逆序输出（不是按大小,就是元素顺序逆序），使用两种方式
def q2():
    li=[]
    while True:
        value=input("请添加数字元素：")
        if value=="over":
            break
        else:
            li.append(value)
    print(li)

    # 方式2
    for i in range(int(len(li)/2)):
        li[i],li[-i-1]=li[-i-1],li[i]
    print(li)


# 3.输入某年某月某日，判断这一天是这一年的第几天
# "闰年能被4整除但不能被100整除，能被400整除"
# "年决定月份的天数，月份决定之前有几个月，日直接相加"
# "闰年和非闰年的'天数/月'可以用list来归纳"
def q3():
    # 闰年月份天数表
    a=[31,29,31,30,31,30,31,31,30,31,30,31]
    # 非闰年月份天数表
    b=[31,28,31,30,31,30,31,31,30,31,30,31]
    year=int(input("年"))
    month=int(input("月"))
    day=int(input("日"))
    monthday=0
    if year%4==0 and year%100 or year%400==0:
        for i in range(month-1):
            monthday+=int(a[i])
        print("今天是本年的第{}天".format(monthday+day))
    else:
        for j in range(1,month):
            monthday+=b[j]
        print("今天是本年的第{}天".format(monthday+day))

# 4.求列表li=[1,4,-5,9,-6]的最大值与最小值，和与平均值
def q4_1():
    li=[1,4,-5,9,-6]
    li.sort()
    max=li[-1]
    min=li[0]
    print(max,min)
    s=0
    for i in li:
        s+=i
    print(s/len(li))

def q4_2():
    li=[1,4,-5,9,-6]
    max=li[1]
    min=li[2]
    for i in li:
        if i>max:
            max=i
        if i<min:
            min=i
    print(max,min)
    print(sum(li)/len(li))

# 5.写程序，输入一个字符，判断是否为关键字 (keyword.kwlist)
import keyword
def q5():
    name=input("请输入一个字符：")
    if name in keyword.kwlist:
        print("字符为python的关键字")
    else:
        print("字符可以作为变量名、类名、函数名使用")

# 6.输入三个整数x,y,z，形成一个列表，请把这三个数由小到大输出
# 用sort方法,自己写排序方法 (提示，获得列表中每次获得的最小值 ,使用索引)
def q6():
    li = []
    for i in range(3):
        a=int(input("请输入整数："))
        li.append(a)
    li.sort()
    print(li)
    for j in li:
        print(j,end=" ")


# 7. 题目：求s=a+aa+aaa+aaaa+aa...a的值
# 其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
# 输入两个值，一个是当前的数字，一个是最大的位数
def q7_1():
    a=input("请输入固定值a")
    b=int(input("请输入最大位数"))
    s=0
    for i in range(1,b+1):
        str=a*i
        s+=int(str)
    print(s)

def q7_2():
    # 规律：每一个数字都是前一个数字*10+a
    a=int(input("请输入固定值a"))
    b=int(input("请输入最大位数"))
    # li=[]
    value=0
    s=0
    for i in range(b):
        value=value*10+a
        # li.append(value)
        s+=value
    # s=0
    # for i in li:
    #     s+=i
    print(s)

# 8. 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，
# 共经过多少米？第10次反弹多高？

def q8():
    a = [100]  # 每个‘反弹落地’过程经过的路程，第1次只有落地（100米）
    h = 100  # 每个‘反弹落地’过程，反弹的高度，第1次为100米
    print('第1次从%s米高落地，走过%s米，之后又反弹至%s米。' % (h, a[0], h / 2))
    for i in range(2, 11):  # 第1次已初始化，再循环9次
        a.append(h)  # 先计算路程，再高度减半，因为一个‘反弹落地’为2个高度
        h = h / 2
        print('第%s次从%s米高落地，共走过%s米，之后又反弹至%s米。' % (i, h, sum(a), h / 2))

# 9.列表通过copy方法复制、切片方法复制、变量赋值方式复制，修改内部元素，画出内存图
def q9():
    "copy和切片性质相同，都是浅拷贝，新建列表中不可变元素不会随原list对应元素改变而改变\
    不可变元素会随原list改变而改变"
    a=[1,2,3,[4,5]]
    b=a
    a[0]=5
    print(b)
    a[3][1]=6
    print(b)


# 10.看一下列表、元组、字符串的整切片指向的对象是什么
def q10():
    "通过id()的验证，list的切片指向一个新的列表，str、tuple指向原体"
    a=["1","2","3","4","5"]
    b="1,2,3,4,5"
    c=(1,2,3,4,5)
    print(id(a),id(b),id(c))
    print(id(a[:]),id(b[:]),id(c[:]))

#test

