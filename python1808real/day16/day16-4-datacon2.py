"""
二、算法的描述
算法：为了解决特定问题而给出的方案。

算法的效率的衡量：
(1)时间复杂度：执行规模（频度）
          最好执行次数
          平均执行次数
          最坏执行次数（为准）

时间复杂度是固定的
介绍几个常用的时间复杂度：
（1）常数时间复杂度O(1)
（2）O(n): 一层循环
（3）O(n^2): 两层循环
（4）O(logn) :当循环的次数翻倍的减少

O(1)<O(logn)<O(n)<O(nlogn)<O(n^2)

(2)空间复杂度：以牺牲空间为代价换取时间。
"""
# while n!=0:
#     print(n)
#     n=n//2

# 1. 查找
# （1）顺序查找
# 从前到后，顺序查找与关键字符相符的元素
def s1(li,key):
    for index,i in enumerate(li):
        if i==key:
            return index
    return -1
print(s1([1,2,3,4,5],10))

# 时间复杂度：O(n)

# （2）折半查找
# 选择中间的元素进行比较，每次都排除一半的元素
# 必要条件：折半查找之前，必须要对元素进行排序
def s2(li,key):
    li.sort()
    start=0
    end=len(li)-1
    while start<end:
        mid=(start+end)//2
        if li[mid]==key:
            return mid
        elif li[mid]<key:# 后半段
            start=mid+1
        else:
            end=mid-1
    return -1
li=[1,44,55,8,6,-5]
print(sorted(li))
print(s2(li,44))


# 时间复杂度O(logn)

# 思考问题
# 1.代码量不一定说明算法好
# 2. 折半查找也不一定好，需要先排序

# 2. 排序
"""
从稳定性上：稳定排序和不稳定排序
1 5 9 -2 9
张三（1）   张三（2）
内容相等的元素如果在排前和排序位置上发生了变化：不稳定排序

冒泡排序（最重要）
选择排序（重要）
插入排序（重要）
希尔排序（了解）
快速排序（掌握）
归并排序（了解）
"""

# 1.冒泡排序
# 俩俩（两个相邻的元素i，i+1）进行比较，根据条件，交换位置，每一次都会选出一个最大或者最小的元素
# 如果是从小到大：每一次都会找到最大的
# 如果是从大到小：每一次都会找到最小的
"""
思路：
（1） n=len（li）
（2） 内循环 j j+1 比较 if li【j】>li[j+1] 交换位置
（3） 外循环  range（n-1）
"""
def sortbuble(li):
    n=len(li)
    for i in range(n-1):
        for j in range(n-1-i):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
            print(li)
        # print(li)
    return li
# sortbuble([23,-8,26,-2,-6,-18,33])
"""
时间复杂度：O(n^2)  最佳的时候可以达到O（n）
稳定性：稳定的排序，
"""

# 2.选择排序
# 每次选择一个最小（最大）的元素，放在前面排好序
# 每次定义一个min_index=0，跟其他元素相比较，找到真正的最小值索引，min_index=真正最小值索引
# li[假的最小值位置] li[真的最小值位置]交换位置
"""
思路：
(1) n=len(li)
(2) 循环
min_index=i for  range(i+1,n) 比较， if li[li] < li[min_index]    min_index=i
(3) 外循环
range（n-1）
"""
def sortchoose(li):
    n=len(li)
    for i in range(n-1):
        min_index=i
        for j in range(1+i,n):
            if li[j]<li[min_index]:
                min_index=j
        li[i],li[min_index]=li[min_index],li[i]
        print(li)
li=[23,-8,26,-2,-6,-18,33]
# sortchoose(li)

# 时间复杂度O(n^2)
# 稳定性：不稳定排序

# 3.插入排序
# 从第二个元素开始，插入到现有列表中（已经排好的队列）
# 每个元素抱着插入之后，列表都是有序的
"""
(1) n=len(li)
(2) 内循环
第0个元素是排好队，
将第一个元素拿出来插入队伍
temp=li[i]
判断： if temp<li[j] li[j+1]=li[j] while
外循环
"""
li=[23,-8,26,-2,-6,-18,33]
n=len(li)
for i in range(1,n):
# i是要插入的元素的位置
#     i=1
    temp=li[i]
    j=i-1
    while temp<li[j] and j>=0:
        li[j + 1] = li[j]
        j-=1
    li[j+1]=temp
    print(li)

# 时间复杂度：O（n^2）
# 稳定性：稳定排序

# 4.希尔
# 最小增量排序，升级版的插入排序
# 使的原来的列表内部先进行分组排序
# 增量不定：没有规则
# 增量：间隔多少 i i+increnment  i+2*increnment
# 规则：从大到小 10 8 6 4 1

def shell(li,increment):
    n=len(li)
    for inc in increment:
        for k in range(inc): # 对增量列表进行循环
            for i in range(inc+k,n,inc): # 分了几个组
                # i是要插入的元素的位置
                # i=1
                temp=li[i]
                j=i-inc
                while temp<li[j] and j>=0:
                    li[j + inc] = li[j]
                    j-=inc
                li[j+inc]=temp
                print(li)
li=[3,-2,5,10,-9,11,7,-1]
increment=[3,2,1]
shell(li,increment)

# 时间复杂度：O(n^2)
# 稳定性：不稳定

# 5.快速排序
# 从列表中选取一个中心点，使的中心点左侧的元素都小于该元素，中心点右侧的都大于该元素
# 递归
def quick1(li):
    n=len(li)
    if len(li)<=1:
        return li
    else:
        mid=0
        small=[]
        bigger=[]
        for i in range(1,n):
            if li[mid]>li[i]:
                small.append(li[i])
            else:
                bigger.append(li[i])
        # small=[i for i in li if i<li[mid]]
        # bigger=[i for i in li if i>li[mid]]
    return quick1(small)+[li[mid]]+quick1(bigger)
li=[3,-2,5,10,-9,11,7,-1]
print(quick1(li))

# 时间复杂度：O（n^2） 最优的时候O（nlogn）
# 稳定度：










