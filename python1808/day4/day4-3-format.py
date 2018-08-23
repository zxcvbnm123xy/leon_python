"""
格式化
"""
print("hello"+" world")
print("hello"+ str(8))
name="tom"
score=90
# print(name+"的成绩是"+score)

# 三种：
"""
1. % 
2. format
3. 3.6之后可以是用f
"""

# 1. %
# %s === str()
# %s代表一个变量占位，后面如果有多个变量，是依次填入
name="tom"
score=90
print("%s的成绩是%s" % (name,score))
print("成绩是%s" % score)

#2.format
#{} 代表一个变量占位，后面有多个变量依次填入
s="{}的成绩是{}"
s="{0}的成绩是{1}"
print(s.format(name,score))
s="{1}的成绩是{0}"
print(s.format(score,name))

#3.f
name="tom"
score=90
print(f"{name}的成绩是{score}")
print("i am 'ok'  and 'addf'")
print(len(""))
print(bool("111"))
print("akdfjalj\\djdlkjf")