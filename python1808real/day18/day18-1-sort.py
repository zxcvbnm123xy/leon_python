"""
快速排序（c语言底层实现）
"""
# 从列表中选出一个中心点pivot，将比中心点小的元素，全部移动到中心点的左侧
#将比中心点大的元素，全部移动到中心点的右侧
def quick(li,left ,right):
    if left<right:
        pivot=partition(li,left,right)
        quick(li,left,pivot-1)
        quick(li,pivot+1,right)

def partition(li,left,right):
    pivot=li[left]
    while left <right:
        while left<right and pivot<li[right]:
            right-=1
        li[left]=li[right]
        while left<right and pivot>li[left]:
            left+=1
        li[right]=li[left]
    li[left]=pivot
    return left
li=[2,-1,22,45,-5,3]
# quick(li,0,len(li)-1)
# print(li)

#稳定性  不稳定


# 归并排序
# 合久必分，分久必合
def merge(li,low ,high):
    if low<high:
        mid=(low+high)//2
        merge(li,low,mid)
        merge(li,mid+1,high)
        merger_sort(li,low,mid,high)

def merger_sort(li,low,mid,high):
    #i是左半部分区域的指针
    #j是右半部分区域的指针
    i=low
    j=mid+1
    temp=[]
    while i<=mid and j<=high:
        if li[i]<=li[j]:
            temp.append(li[i])
            i+=1
        else:
            temp.append(li[j])
            j+=1
    while i<=mid:
        temp.append(li[i])
        i+=1
    while j<=high:
        temp.append(li[j])
        j+=1
    li[low:high+1]=temp
li=[2,-1,22,45,-5,3]
merge(li,0,len(li)-1)
print(li)
#时间复杂度：O(nlogn)
#稳定性 ： 稳定排序
#空间复杂度O(n)