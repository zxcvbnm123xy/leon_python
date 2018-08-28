# 1.
# 研究一下min，max、sum函数，看看传入一个列表是否可以使用？传入多个参数形式是否可以使用？自己写一个函数，使得sum也能跟max和min一样，可以传入多个参数
# sum((1, 2, 3))
li=[1,2,3]
print(min(li)   )
print(max(li)   )
print(sum(li)  )

print(min(1,2,3))
print(max(1,2,3))
# print(sum(1,2,3))

def sum2(* n):
    return sum(n)
print(sum2(1,2,3))
print(sum2(* li))  # ([1,2,3],)

#
# 2.
# 编写函数，第一个参数指定今天是星期几（1 ~ 7），第二个参数指定天数n，返回n天后是星期几。
# 1 星期一  2星期2   ...7 星期天
def which_day(today_which,n):
    d=(today_which+n)%7
    if d==0:
        return 7
    return d
print(which_day(2,5))

# 计算机：存储(内存和硬盘)、控制器、计算中心、输入输出
# 控制器、计算中心：CPU
# 存储：内存和硬盘
# IO


# 3.
# 证明运算符优先级高会影响结合性，但不会像数学上那样，先进行计算。
# 例如：a + b * c，会首先计算a（使用函数来证明）。
3 + 4 * 5
def a():
    print("a函数执行")
    return 3
def b():
    print("b函数执行")
    return 4
def c():
    print("c函数执行")
    return 5
a()+b()*c()

#
#
# 4.
# 写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，
# 并将新内容返回给调用者，否则返回“不符合要求”提示
def myfun(seq):
    n=len(seq)
    if n>2:
        return seq[:2]
    else:
        return "不符合要求"
print(myfun([1,2,3,4,5]))
print(myfun([1]))

#
# 5. 将之前写过的列表的排序，写成函数，实现传入一个列表能够进行排序的功能。
# 排序
# 思路：每次都找到列表中的最小值。
# 先假设第一个值是最小值，然后再跟其他值比较 ，找到真正最小值，
# 找到真正的最小值之后，再进行位置交换
li=[22,4,5,-6,7,11,3]
# 第一次
# min=0
# for i in range(1,len(li)):
#     if li[i]<li[min]:
#         min=i
# li[min],li[0]=li[0],li[min]
# print(li)
#
# # 第二次
# min=1
# for i in range(2,len(li)):
#     if li[i]<li[min]:
#         min=i
# li[min],li[1]=li[1],li[min]
# print(li)
def sortlist(li):
    for j in range(len(li)-1):
        min = j
        for i in range(j+1, len(li)):
            if li[i] < li[min]:
                min = i
        li[min], li[j] = li[j], li[min]
        # print(li)
    return li
print(sortlist(li),li)