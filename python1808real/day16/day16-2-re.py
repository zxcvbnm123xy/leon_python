"""
第十五章 正则表达式
"""
# 一、相关概念和用法
# 正则表达式，可以对【指定的字符串】跟【模式】之间进行匹配的工具。
# 通过正则表达式的匹配，可以获得匹配的结果

# 模式：
# 普通字符串： 完全按照字符串的内容进行匹配
# 特殊意义的字符： 正则表达式的特殊字符串，是这一章的主要内容

# 普通字符串 功能跟in 操作符类型  ：普通字符串 in 指定的字符串
# 在python中正则表达式是用re模块来实现的
import re
#
# 第一个参数：模式字符串
# 第二个参数：待搜索字符串（指定的字符串）
# re.search返回值：如果能够匹配，那么返回正则表达式对象，如果不能匹配，则None
# print("abc" in "jeopteljkjfabcsdljf")
r=re.search("abcd","jeopteljkjfabcsdljf")
# 匹配对象下的group函数：返回匹配的结果
# r.group()
# print(r)
# 匹配成功
if r:
    print(r.group())
# 没有匹配成功
else:
    print("匹配不成功")



# 二、特殊意义的字符
# 1. 字符相关
# （1）. 默认模式下，匹配除了\n以外的【单个】字符
#     可以通过修改flaggs标志来修改模式，匹配的时候所有任意一个字符（包括\n）
r=re.search("a.b","diopa\nbewjrj",re.DOTALL)
if r:
    print(r.group())
else:
    print("匹配不成功")

# (2)[]匹配中括号中任意【一个】字符，[]中可以有多个字符，也可以有单个字符，
# 也可以有区间使用-表示从x到y
# 如果匹配的时候，需要匹配-，则需要使用转义字符\，或者可以将-放到[]的两端
# r=re.search("a[abcdef0123]b","diopa4bewjrj")
# r=re.search("a[A-Z]b","diopafbewjrj")
# r=re.search("a[01\-2]b","diopa-bewjrj")
# r=re.search("a[-012]b","diopa[bewjrj")
# if r:
#     print(r.group())
# else:
#     print("匹配不成功")

# (3)^，只有紧邻[^]才好用，表示匹配不在[]中的任意一个字符
# 跟[]取反
r=re.search("a[^012]b","diopa0bewjrj")
if r:
    print(r.group())
else:
    print("匹配不成功")

# (4)\d unicode十进制数字，不限于0-9
r=re.search("a\db","diopacbewjrj")
if r:
    print(r.group())
else:
    print("匹配不成功")

# (5)\D 跟\d取反
r=re.search("a\Db","diopa1bewjrj")
if r:
    print(r.group())
else:
    print("匹配不成功")

#(6)\w unicode中单词字符 a-z A-Z _ 0-9 汉字
r=re.search("a\wb","diopa中bewjrj")
if r:
    print(r.group())
else:
    print("匹配不成功")
#(7)\W 跟\w取反
r=re.search("a\Wb","diopa$bewjrj")
if r:
    print(r.group())
else:
    print("匹配不成功")

# (8)\s 空白 \r\n\t
# r=re.search("a\sb","diopa    bewjrj")
r=re.search("a\sb","diopa\rbewjrj")
if r:
    print(r.group())
else:
    print("匹配不成功")

# (9)\S \s的取反
r=re.search("a\Sb","diopa\rbewjrj")
if r:
    print(r.group())
else:
    print("匹配不成功")

print("============")
#2.跟次数相关
# （1）* 匹配前面的字符0或者多次，修饰前面的字符串，不能单独使用
# 贪婪匹配：尽可能多的匹配
# 会一直往下匹配，一直匹配到不匹配为止。
r=re.search("ba*","baa")
if r:
    print(r.group())
else:
    print("匹配不成功")

# a*代表0或者多个a
r=re.search("a*","aab" )
# r=re.search("a*","aaa")
if r:
    print(r.group())
else:
    print("匹配不成功")


#(2) + 匹配1或者多次
r=re.search("ba+","baaaaaaaac" )
if r:
    print(r.group())
else:
    print("匹配不成功")

# (3)? 匹配0 或者1次
# r=re.search("ba?","bc" )
r=re.search("a?","bc" )
if r:
    print(r.group())
else:
    print("匹配不成功")

# (4) {m} 精确匹配m次  : 非贪婪匹配
r=re.search("a{2}","aaaaa" )
if r:
    print(r.group())
else:
    print("匹配不成功")

#（5）{m,} 匹配至少m次
# r=re.search("ba{2,}","baaaaa" )
r=re.search("ba{2,}","ba" )
if r:
    print(r.group())
else:
    print("匹配不成功")

# (6){,n} 最多匹配n次
# r = re.search("ba{,2}", "ba")
# r = re.search("ba{,2}", "baaaaa")
r = re.search("ba{,2}", "b")
if r:
    print(r.group())
else:
    print("匹配不成功")

# (7){m,n}  匹配m到n次
r = re.search("ba{2,4}", "baaaaaaaaaaa")
if r:
    print(r.group())
else:
    print("匹配不成功")

# （8）X?  x代表以上的匹配模式（精确匹配除外）
# 将贪婪匹配变成非贪婪匹配
# 尽可能少的匹配
r=re.search("a+?","aab" )
if r:
    print(r.group())
else:
    print("匹配不成功")

# 练习：
# 1. 匹配任意三个字符
r=re.search(".{3}","12344" )
if r:
    print(r.group())
else:
    print("匹配不成功")
# 2. 匹配任意一个乃至更多字符
r=re.search(".+","123442344" )
if r:
    print(r.group())
else:
    print("匹配不成功")

# 3.边界相关
# （1） ^ 匹配字符串的开头
# 通过修改多行模式来匹配多行的开头，
# r=re.search("^张","某\n张三丰" ,re.MULTILINE)
r = re.search("^张{1,3}", "三丰\n张四丰",re.MULTILINE)
if r:
    print(r.group())
else:
    print("匹配不成功")

# (2) $匹配字符串结尾
r = re.search("\w+\.com$", "http://wwwb.com")
if r:
    print(r.group())
else:
    print("匹配不成功")

# （3）\A 仅匹配字符串的开头，永远是单行模式
# （4）\Z 仅匹配字符串的结尾，永远是单行模式

# （5）\b 边界的概念，unicode跟非unicode之间就是边界
# r = re.search(r"\bcd", "cd")
r = re.search(r"\bcd", "acd")
if r:
    print(r.group())
else:
    print("匹配不成功")

# （6）\B 匹配非边界 \b的取反



# 4.组的相关
# （1）() 对小括号内的字符进行分组，分组之后，可以对内容进行单独提取
# ()有两个作用，第一个对括号内的内容进行整体操作    第二个通过小括号进行单独提取元素
# r = re.search(r"cab+", "cabab")
r = re.search(r"c(ab)+", "cabab")
if r:
    print(r.group())
    print(r.group(1)) #参数代表第几个小括号，从1开始
else:
    print("匹配不成功")

# 例子
r = re.search(r"<b>(.*)</b>", "<b>一些加粗的内容</b>")
if r:
    print(r.group())
    print(r.group(1)) #参数代表第几个小括号，从1开始
else:
    print("匹配不成功")

# 例子
r = re.search(r"([0-9]{3,4})-([0-9]{7,8})", "010-12345678")
if r:
    print(r.group())
    print(r.group(1)) #参数代表第几个小括号，从1开始
    print(r.group(2)) #参数代表第几个小括号，从1开始
else:
    print("匹配不成功")

# （2）\number,number代表分组指定的序号
# 只希望取成对的标签中的内容
r = re.search(r"<([a-zA-Z]+)>(.*)</\1>", "<b>一些加粗的内容</a>")
if r:
    print(r.group())
    # print(r.group(1)) #参数代表第几个小括号，从1开始
else:
    print("匹配不成功")

# （3）(?P<name>)  对()分组进行命名
# r = re.search(r"<(?P<tt>[a-zA-Z]+)>(.*)</(?P=tt)>", "<b>一些加粗的内容</b>")
# if r:
#     print(r.group())
#     # print(r.group(1)) #参数代表第几个小括号，从1开始
# else:
#     print("匹配不成功")

# （4）| 用来连接两个并列模式的字符串，匹配其中的一个即可
# [abcd]  如果希望表示ab和cd 可以使用|
# 误区：abcef  abdef
r = re.search(r"ab(c|d)ef", "abdef")
# r = re.search(r"abc|def", "acd")
if r:
    print(r.group())
else:
    print("匹配不成功")
# .com .net  .edu
# \.com|edu|net
# \.jpg|bmp|png


# 5. 控制标记
# re.DOTALL  : 支持所有字符
# re.MULTILINE:支持多行
# re.IGNORECASE: 忽略大小写
# 都可以当做flag标记
r = re.search(r"abc", "ABC",re.IGNORECASE)
if r:
    print(r.group())
else:
    print("匹配不成功")


# 三、相关的属性和方法
# 1.re模块下的函数
# （1）compile() 会生成一个正则表达式对象
# 一般匹配多次的时候，会先形成一个正则表达式对象
# 两个参数，一个是正则表达式，一个是控制标记
reobj=re.compile("abc+")
m=reobj.search("abcccc")# 得到匹配之后的对象
if m:
    print(m.group())

# (2)re.search() 学过 用来匹配正则表达式和待匹配字符串,如果匹配，只找一次
# (3)re.findall() 返回所有匹配的内容，形成一个列表
li=re.findall("[0-9]","d34r6u7")
print(li)

c="<div>中秋快到了</div><div>十一也快到了</div>"
li=re.findall("<div>(.*?)</div>",c)
for i in li:
    print(i)

# (4)finditer 跟findall类似，返回的是迭代器
# re.finditer()
# li=re.finditer("[0-9]","d34r6u7")
# for i in li:
#     print(i.group())

# (5)re.split()
#升级版的切割
s="a ncd d   a d         d"
print(s.split(" "))
# re.split(正则表达式,待匹配字符串)
print(re.split(" +",s))

# (6)re.sub() 跟字符串中replace，升级的replace
# re.sub(正则表达式，要替换成的内容，待匹配的字符串)
# print(re.sub(" +"," ","a ncd d   a d         d"))

# 2.正则表达式对象
# 当匹配成功之后，会返回的正则表达式对象
# （1）string属性 待匹配的文本
#  (2)re属性  正则表达式
# （3）搜索文本的开始和结束位置
#  (4)group返回匹配后字符串
#  (5)groups ,返回所有分组的匹配结果
# （6）start end 匹配字符串在原始字符串中的位置
m=re.search(r"(a+)-(b+)","123aaaa-bbbbb1234")
if m:
    print(m.string)
    print(m.re)
    print(m.pos)
    print(m.endpos)
    print(m.group())
    print(m.group(1),m.group(2))
    print(m.groups())
    print(m.start())
    print(m.end())
    print(m.span())
    print(m)


# 案例：

l="""
<table border=1>
  <tr>
    <th>姓名</th>
    <th>年龄</th>
    <th>性别</th>
  </tr>
  <tr>
    <td>张三</td>
    <td>20</td>
    <td>男</td>
  </tr>
  <tr>
    <td>李四</td>
    <td>30</td>
    <td>女</td>
  </tr>
</table>
"""
# 使用正则表达式获取<tr></tr>之间内容
res_tr=r"<tr>(.*?)</tr>"
m_tr=re.findall(res_tr,l,re.IGNORECASE|re.DOTALL|re.MULTILINE)
for line in m_tr:
    # 获取td中的内容
    res_td=r"<td>(.*?)</td>"
    m_td=re.findall(res_td,line,re.IGNORECASE|re.DOTALL|re.MULTILINE)
    for i in m_td:
        print(i)