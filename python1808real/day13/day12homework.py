# 1.使用random.random()函数实现返回[a, b]之间的整数。(a <=x<=b)  randint(a,b)
#
#
"""
random.randomint(a,b)   a<=x<=b
random.random()         0<=x<1
[a,b]                   a,(b-a)+a   #只要让你b-a是随机产生的
问题：
1.[a,b)
2.需要得到一个整数，目前是一个小数
（1）向上取整 ceil
a    a+math.ceil（random.random()*(b-a)）
a,b = 0,100
0     0.999*(100-0)      99.9-----100

（2）向下取整   floor
a    a+math.floor（random.random()*(b-a)）
a,b=0,100
0     0.999*(100-0)  99.9-----99


"""
# 2.自行计算常数e的近似值。（1 / 0! + 1 / 1! + 1 / 2! + 1 / 3! + ……）
#
# 3.编写一个抽奖的函数，返回（0-3），0表示未中奖，1-3表示1-3等奖。1等奖概率为1%，二等奖5%，三等奖10%，其余为未中奖。
#
# 4.输入某一天，返回该天距离下一个国庆还有多少天。如果当天就是国庆，则返回0。
#
# 5.输入某一天（年月日），返回该天是星期几。
#
# 6.输入年月，打印该月份的日历。