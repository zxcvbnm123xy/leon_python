"""
第四章 数据类型 （字符串、字节）str
"""
"""
字符串：就是由字符组成的序列，字符串中的每一个元素还是字符串。
特性：字符串是不可变的序列类型。字符串的元素是有序的。
"""
# 一、字符串的创建
# 三种方式
"""
单引号
双引号
三引号
"""
# 使用单引号和双引号创建字符串，使用方式几乎一致
# 单引号和双引号交替使用可以达到输出对方的效果
s="helloworld"
s="i am 'ok'"
print(s)
s2='i am "ok"'
print(s2)

# 单引号和双引号定义字符串，一般都在一行定义 ，否则需要续行符（\）
a="引号和双引号定义字符串，一般都在引号和双引号定义字符串， "\
"一般都在引号和双引号定义字符串，一般都在引号和双引号定义字符串，一般都在"
print(a)

b="天行健，君子以自强不息。\n地势坤，君子以厚德载物"
print(b)

#三引号定义字符串，自带换行，但是三引号不是注释。
c="""
天行健，君子以自强不息。
地势坤，君子以厚德载物
"""
print(c)

# 练习：输出一首诗，使用双引号和三引号分别输出。

# 定义空字符串，不是None
str_null=""
print(type(str_null))
print(type(None))

# 二、字符串的转义序列(将特殊的字符转义)
s="i am 'ok'"
# 双引号，单引号的转义使用\,放到要转义字符的前面
s="i am \"ok\""
print(s)

# \n 换行
# \r 回车
# \n\r
# window下：
# \r，要回到当前行的行首，不会换到下一行，如果直接输出，会将之前的内容覆盖。
print("aaaa\rbbbbb")
print("aaaa\n\rbbbbb")

#\n ，代表换行，换到当前位置的下一行(常用)
print("aaa\nbbbb")

# r:在字符串定义的前面加r，能够让字符串原样输出
print(r"aaa\bbbbbb")


# 三、字符串的操作
"""
1. 运算符
2. 索引
3. 切片
"""

# 1. 运算符  +  *   in  not in    is  is not   ==  >  < !=
# + 合并  新创建字符串进行合并
a="abc"
b="bcd"
print(a,b,a+b,a,b)

# * 重复，返回的是新字符串
print(a*3,a)
print(a*3+b*2)

#in  not in 成员运算符
print("ab"  in a)
print("ac"  in a)

# is  is not 身份运算符
a="abc"
b="abc"
c=b
print(a is b)
print(c is a)

print(a ==b )
print(a ==c )


# 按元素进行比较，按照元素的ascii码进行比较
# 逐个比较
print("abc"<"abcd")
print(ord("a"))
print(ord("b"))

# 2. 索引
# 获取字符串中的单个字符串，需要使用索引
# 格式：字符串名[index]: index 可以是正数、负数、0
# 第一个元素：索引从0开始
# 正数：从左到右
# 负数：从右到左，最后一个元素是-1
# 索引是不能越界，越界会报异常。
s="abcdefg"
print(s[0])
print(s[3])
print(s[-3])
# print(s[100])
# len(o):获取字符串的长度
print(len(s))
# 索引范围： [-len(s)---len(s)-1]
# 最后一个元素：s[len(s)-1]   s[-1]

# 字符串中的元素不能修改
# s[2]="6"


# 3. 切片：获得字符串中的多个元素（按照某一个规则获得指定区域的元素）
# 格式：字符串名[start:end]
# 切片包含start，但是不包含end，到end-1
# start 和end都可以取正数、负数、0
# 区别在于方向
# start:省略，默认是0
# end：省略，默认的len(s),千万注意，不是-1
s="abcdefg"
print(s[0:3])  # end-start=截取的长度
# print(s[0:1],s[1:3])
print(s[-1:-3],"dddd")
print(s[-3:-1],"ccc")

print(s[:3],s[0:3])
print(s[1:],s[0:len(s)])
# print(s[1:],s[0:-1])

# 切片是新创建字符串(非整切片)
# 字符串的整切片指向的就是字符串本身的对象，不是新创建对象
s1=s[1:3]
print(s1,id(s1))
s2=s[:]
print(id(s[:]),id(s),id(s2))


#练习：使用字符串的切片 对日期进行获取  2018-08-20
d="2018-08-20"
year=d[:4]
print(year)
month=d[5:7]
print(month)
day=d[8:]
day=d[-2:]
print(day)


#4. 字符串的相关方法
st="abcdabcd"
# (1)count(str,start,end)统计 返回参数字符串在原串中出现的次数
# 当不写start和end参数时，默认统计的是按原字符串统计
print(st.count("a"))
# start=1 end=5  范围从1---4
print(st.count("a",1,5))
# 如果只传递一个参数 那么认为是start，结束默认为len(st)  范围是从1--len(st)
print(st.count("a",1))

# 跟切片一样，当索引（下标）超过范围时，不会报错。
print(st.count("a",20,50))

# （2） index 查找，如果查找到则返回原中的位置，如果找不到会报错
# 默认从左到右查找，查找第一次出现的位置
st="abcdabcd"
print(st.index("b"))
# print(st.index("b",2,5))
print(st.index("b",2))

# (3)find 查找，返回查找内容再原串中的位置，如果找不到不报错，会返回-1
st="abcdabcd"
print(st.find("b"))
print(st.find("b",2,5))

# 如果查找的是子串，会返回子串中第一个字符出现的位置
st="abcdabcd"
print(st.find("bc"))
print(st.find("bd"))

# （4） join：拼接字符串：将序列中的各个元素按照字符串连接。
st="abcd"
a="-"
print(a.join(st))

# (5)replace: 替换:会新创建字符串进行存储，替换结果是replace的返回值
# old:需要替换的内容
# new：替换成的内容
# count：替换的最大次数，如果不写，会将字符中符合的字符全部替换
# 会从左到右的顺序，按照替换的次数进行替换
st="abcdabcd"
print(st.replace("a","-",1))
print(st.replace("a","-",4),st)

#（6）strip 剪切，从两端去掉指定的符号
st=" abcd  "
# strip参数不写，则默认去掉空格
print(st.strip())
# 去掉两端符合条件的字符串（按挨个检索），一直去掉到不符合条件的位置。
st="aafbbcdeeafaf"
print(st.strip("a"))
print(st.strip("af"))

# 从左边剪切
print(st.lstrip("af"))
# 从右侧剪切
print(st.rstrip("af"))

#（7）split 切割：切割完的字符就没有了。
# 按照切割的参数，一分为二
# 返回值是列表
st="ab cd ef  gh d"
print(st.split(" "))
#如果split中不写参数，默认按照空格切割，会将所有的空格都切割掉。
print(st.split())

st="abababaabbaabb"
print(st.split("a"))

#(8)upper  lower
print("abcd".upper())
print("ABCDdd".lower())

# (9)isnumeric: 判断是不是数值类型
print("8".isnumeric())
print("a".isnumeric())

#(10)isalpha: 判断是不是字符
print("8".isalpha())
print("a".isalpha())

#(11)center(width,char)
#width：占位
#char: 填充的字符
s="hello world"
# 当字符串长度是奇数，填充会从右侧开始
# 当字符串长度是偶数，填充会从左侧开始
print(s.center(13,"*"))
s="hell"
print(s.center(5,"*"))
