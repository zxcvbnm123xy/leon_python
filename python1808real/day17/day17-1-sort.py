
# 2. 排序
"""
从稳定性上：稳定排序和不稳定排序
1  5  9  -2  9
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
# 俩俩（两个相邻的元素i ,i+1）进行比较，根据条件，交换位置，每一次都会选出一个最大（最小）的元素
# 如果小--大：每一次都会找到最大
# 如果大--小：每一次都会找到最小
"""
思路：
（1） n=len(li)
 (2) 内循环  j j+1 比较  if li[j]>li[j+1]  交换位置  
 (3) 外循环  range(n-1)
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
时间复杂度：O(n^2)   最佳的时候可以达到O(n)
稳定性： 稳定的排序
"""


# 2. 选择排序
# 每次选择一个最小（最大）的元素， 放在前面排好序。
# 每次定义一个min_index =0，跟其他元素相比较 ，找到真正的最小值的索引 min_index=真正的最小值索引
# li[假的最小值位置] li[真的最小值]交换位置。
"""
思路：
（1）n=len(li)
(2)内循环
min_index=i   for range(i+1,n)  比较 if li[i] < li[min_index]  min_index=i
（3）外循环
range(n-1)
"""
def sortchoose(li):
    n=len(li)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if li[j]<li[min_index]:
                min_index=j
        li[i],li[min_index]=li[min_index],li[i]
        print(li)
li=[23,-8,26,-2,-6,-18,33]
# sortchoose(li)

# 时间复杂度 O(n^2)
# 稳定性  不稳定排序

# 3. 插入排序
# 从第二个元素开始，插入现有列表中（已经排好队的列表），
# 每个元素保证插入之后，列表都是有序的
"""
（1）n=len(li)
(2) 内循环
第0个元素是排好队，
将第1个元素拿出来插入好队伍
temp=li[1]
判断：if temp<li[j]  li[j+1]=li[j]  while
外循环
"""
# li=[23,-8,26,-2,-6,-18,33]
# n=len(li)
# for i in range(1,n):
#     # i 是要插入的元素的位置
#     # i=1
#     temp=li[i]
#     j=i-1
#     while temp<li[j] and j>=0:
#         li[j + 1] = li[j]
#         j-=1
#     li[j+1]=temp
#     print(li)

# 时间复杂度：O(n^2)   最优O(n)
# 稳定性：稳定排序


# 4. 希尔
# 最小增量排序，升级版的插入排序
# 使得原来的列表内部先进行分组排序
# 增量不定：没有规则
# 增量：间隔多少  i  i+increnment   i+2*increnment
# 规则：从大小  10  8  6  4  1

def shell(li,increment):
    n=len(li)
    for inc in increment:# 对增量列表
      for k in range(inc):# 分几个组
        for i in range(inc+k,n,inc):
            # i 是要插入的元素的位置
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
# shell(li,increment)
# 时间复杂度： O(n^2)
# 稳定性:  不稳定

#5. 快速排序
# 从列表中选取一个中心点，使得中心点左侧的元素都小于该元素，中心点右侧的元素都大于该元素。
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
    return quick1(small) + [li[mid]]  +quick1(bigger)
li=[3,-2,5,10,-9,11,7,-1,7]
print(quick1(li))

#时间复杂度: O(n^2)  最好O(nlogn)
# 稳定：取决于算法。
