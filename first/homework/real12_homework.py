# 1.使用random.random函数实现返回[a, b]或[a, b)之间的整数。(a <=b)
#
#
import random
import math
x=random.random()
def x(a,b):
    return a+math.floor(random.random()*(b-a+1))
print(x(0,1))

# 2.自行计算常数e的近似值。（1 / 0! + 1 / 1! + 1 / 2! + 1 / 3! + ……）
#
s=0
for i in range(1000):
   s+= 1/math.factorial(i)
print(s)
# 3.编写一个抽奖的函数，返回（0-3），0表示未中奖，1-3表示1-3等奖。
# 1等奖概率为1%，二等奖5%，三等奖10%，其余为未中奖。
#
x=random.choices([0,1,2,3],weights=[0.84,0.01,0.05,0.1])
if x==[1]:
    print("牛X啊，老铁。一等奖！")
elif x==[2]:
    print("二等奖！")
elif x==[3]:
    print("三等奖！")
else:
    print("谢谢惠顾")
# 4.输入某一天，返回该天距离下一个国庆还有多少天。如果当天就是国庆，则返回0。
#
from datetime import date
def q3():
    year=int(input("请输入年份："))
    month=int(input("请输入月份："))
    day=int(input("请输入日："))

    d=date(year,month,day)
    d10_1=d.replace(month=10,day=1)
    if d>d10_1:
        d10_1=d10_1.replace(year=d.year+1)
    print(abs(d10_1 - d).days)

# 5.输入某一天（年月日），返回该天是星期几。
#
def q4():
    year=int(input("请输入年份："))
    month=int(input("请输入月份："))
    day=int(input("请输入日："))
    d = date(year, month, day)
    d.weekday()
    days=["周一","周二","周三","周四","周五","周六","周日"]
    print(days[d.weekday()])
# 6.输入年月，打印该月份的日历。
year=int(input("请输入年份："))
month=int(input("请输入月份："))
month_day=[0,31,28,31,30,31,30,31,31,30,31,30,31]
if year%4==0 and year%100!=0 or year%400==0:
    month_day[2]=29

for i in ["日","一","二","三","四","五","六"]:
    print(i,end="\t")
print()
# 判断当前月份，1 号是星期几，前面就有几个空格
day1=date(year,month,1)
day1weekday=day1.weekday()
if day1weekday<6:
    for i in range(day1weekday+1):
        print(end="\t")
# 从1号开始输出到最后一天
for i in range(1,month_day[month]+1):
    if day1weekday==7:
        day1weekday=0
    elif day1weekday==6 and i!=1:
        print()
    print(i,end="\t")
    day1weekday+=1
