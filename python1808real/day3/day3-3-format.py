"""
格式化
"""
# 三种：%  format   f
# 1. %
# %s  str()  对非字符类型转换成字符串
# %f  对浮点数保留有效位数
# 一个%s 代表一个变量
print("我的爱好是%s" % "足球")
print("我的爱好是%s、%s、%s" % ("足球","排球","乒乓球") )
print("hello%s-%s" % (1,2))

# %ns---n是整数，代表占位符n
# 如果占位n<变量字符串的长度，不会截断，会原样输出
print("%10s" % "djldkjflasdufldkjf")
# 如果n>变量字符串的长度，会默认按照右对齐
print("%10s" % "dj")
# 如果是左对齐，直接将正数改成负数
print("%-10s" % "dj")

#%.ms----  .m可以是小数，代表保留几个小数位，如果是字符串s则代表要截取几位
print("%.2s" % "djldkjflasdufldkjf")

# %m.ns m是占位符  是整数  n是取n位，默认右对齐
print("%10.2s" % "hello world")
print("%-10.2s" % "hello world")

#%f 格式化浮点数
# %m.nf m 占用多少位，n保留的小数位数
print("%.f" % 3.14159)
print("%0.f" % 3.14159)
print("%0.0f" % 3.14159)

# 保留小数时，四舍五入
print("%.2f" % 3.14159)
print("%.2f" % 3.14559)
print("%.20f" % 3.14559)

print("%8.2f" % 3.14559)
# %f还可以指定是否需要用0补齐
print("%08.2f" % 3.14559)


# 2.format
# {} 代表一个变量
print("this is {},that is {}".format("tom","jerry"))
print("this is {0},that is {1}".format("tom","jerry"))
print("this is {1},that is {0}".format("tom","jerry"))
print("this is {a},that is {b}".format(a="tom",b="jerry"))
print("this is {b},that is {a}".format(a="tom",b="jerry"))

#  格式化格式:{[参数/索引]:[对齐方式][整数].[保留小数位数][s/f]}.format(参数)
print("{} and {}".format("hello","world"))
print("{:10} and {:10}".format("hello","world"))  #默认是左对齐
print("{:<10} and {:<10}".format("hello","world"))
print("{:>10} and {:>10}".format("hello","world"))
print("{:^10} and {:^10}".format("hello","world"))
print("{:^10.2} and {:^10.3}".format("hello","world"))

# f
print("{:10.2} and {:10.2f}".format(10.123,1.123))
print("{:>10} and {:10} and {:10f}".format("hello",10.123,1.123))


# 3.
a="篮球"
print(f"我的爱好是{a}")








