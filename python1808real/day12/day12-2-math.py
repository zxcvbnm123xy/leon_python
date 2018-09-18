"""
第十一章 模块和包
三、数学模块math
四、random
五、时间
"""
# math
import math
# 1.圆周率
print(math.pi)

# 2. 数学常数
print(math.e)

# 3.向上取整
print(math.ceil(5.3))
print(math.ceil(-5.3))

# 4.向下取整
print(math.floor(5.3))
print(math.floor(-5.3))

# 5.返回e的x次幂
print(math.exp(1))

# 6.返回x的y次幂
print(math.pow(2,7))

# 7.返回以base为底，x的对数,base默认以e为底
# print(math.log(x,base))
print(math.log(100,10))

# 8.fabs返回浮点类型的绝对值
print(abs(-1.0))
print(math.fabs(-3.4))
print(math.fabs(-3))

# 9.factorial 阶乘
print(math.factorial(3))

# 10. 取余，商是正数：向下取整；商是负数，向上取整
print(math.fmod(5,3))
print(math.fmod(5,-3))

# 11.求累加和，结果是浮点类型
print(math.fsum([1,2,3,4]))

# 12. 返回平方根
print(math.sqrt(100))

# 13.返回最大公约数
print(math.gcd(12,15))

