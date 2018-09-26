# 1.将一个字符串中每一个a替换成一个b。
import re
x="dhasfhdjadfdaaabb"
print(x.replace("a","b"))
print(re.sub("a","b",x))


# 2.提取<div><div>aaa</div></div>   div中的内容
m=re.search(r"<div>([^<>]*)</div>","<div><div>aaa</div></div>")
if m:
    print(m.group())
    print(m.group(1))

# 3.校验用户姓名：只能输入1-30个以字母开头的字串
m=re.search(r"^[a-zA-Z].{0,29}$","ADMIN")
if m:
    print(m.group())


# 4.创建一个正则表达式，正确格式为邮政编码
m=re.search(r"^[0-9]{6}$","000000")
if m:
    print(m.group())


# 5.身份证号
# 	xxxxxx yyyy MM dd 375 x|0     十八位
# 	xxxxxx   yy MM dd 750         十五位
m18=r"[1-9][0-9]{5}(18|19|20)([0-9]{2})(0[1-9]|10|11|12)([0-2][1-9]|30|31|10|20)[0-9]{3}[0-9Xx]"
m15=r"[1-9][0-9]{5}[0-9]{2}(0[1-9]|10|11|12)([0-2][1-9]|30|31|10|20)[0-9]{3}"
m=re.search(m18,"21090218900131555x")
if m:
    print(m.group())


# 
# 6.有html信息
html="""
<td>
<a href="https://www.baidu.com/articles/zj.html" title="浙江省">浙江省主题介绍</a>
<a title="贵州省" href="https://www.baidu.com//articles/gz.html" >贵州省主题介绍</a>
</td>
"""
# 	1. 获得<a href></a>标签所有的内容
mm=re.findall(r"<a .*?>(.*?)</a>",html,re.IGNORECASE|re.MULTILINE|re.DOTALL)
for i in mm:
    print(i)

# 	2. 获得a标签的url的内容
murl=re.findall(r"<a .*?href=\"(.*?)\".*?</a>",html,re.IGNORECASE|re.MULTILINE|re.DOTALL)
for i in murl:
    print(i)

#
# 7. 获得这个链接下的参数
url = 'http://localhost/test.py?a=hello&b=world&c=ddd'
#方式一：
values=url.split("?")[-1].split("&")
print(values)

# 方式二：
# 	2. 获得a标签的url的内容
murl=re.findall(r"(\w+=[^&]*)",url)
for i in murl:
    print(i)


#
# 8. 使用递归解决折半查找
def search(li,key,low,high):
    mid=(low+high)//2
    if key==li[mid]:# 找到
        return mid
    if low>high:
        return -1
    if key<li[mid]:
        return search(li,key,low,mid-1)
    else:
        return search(li, key, mid+1, high)
#
li=[4,11,34,66,74,78,99]
print(search(li,75,0,len(li)-1))