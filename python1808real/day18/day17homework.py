# 1	改写冒泡排序，将冒泡排序的最好时间复杂度改成O(n)。
#  俩俩比较，符合条件，交换
def sortbubble(li):
    n=len(li)
    didswap=False
    for i in range(n-1):
        for j in range(n-1-i):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
                didswap=True
        if didswap==False:
            return li
# li=[3,54,66,7,9,-8,-1]
li=[-8, -1, 3, 7, 9, 54, 66]
# sortbubble(li)
# print(li)


# 2	将所有的排序使用降序实现。
# 大--小
# 选择
# 每一次都选出一个max
def choosesort(li):
    n=len(li)
    for i in range(n-1):
        max_index=i
        for j in range(i+1,n):
            if li[max_index]<li[j]:
                max_index=j
        li[i],li[max_index]=li[max_index],li[i]
li=[3,54,66,7,9,-8,-1]
choosesort(li)
print(li)

# 插入
# 第0个元素认为是排好序，将后面的元素依次插入到排好队的队伍中。
li=[3,54,66,7,9,-8,-1]
#[54,54,3,7,9,-8,-1]
def insertsort(li):
    n=len(li)
    for i in range(1,n):
    # 第0个元素认为是排好序的
    # 第一排序，排第一个元素
    #     i=1
        temp=li[i]
        j=i-1
        while temp>li[j] and j>=0:
            li[j+1]=li[j]
            j-=1
        li[j+1]=temp
    return li
insertsort(li)
print(li)





# 3	能够手写排序算法。（面试） 冒泡、选择、插入、快速（最好）
