"""时间模块"""
# 一、time包：都是关于时间的操作
import time
# UTC：世界标准时间，本初子午线上时间
# 1. timezone: 返回与UTC时间相差的秒数
print(8*60*60)
print(time.timezone)

# 2.time.time()返回从新纪元到当前时间走过的秒数，小数是微秒
# 新纪元：unix产生时间1970-1-1
print(time.time())

# 3.time.localtime([s])返回从新纪元走过的s秒之后的时间，返回的是时间元组
# 如果不写s，默认返回的是本地当前时间
print(time.localtime(1))
print(time.localtime())

# 4.gmtime([s]) 返回从新纪元走过的s秒之后的时间, 返回值是utc时间
print(time.gmtime(1))
print(time.gmtime())

# 5. time.mktime(tuple) 将时间元组转换成秒数，秒数---从新纪元到tuple时间元组的时间
t=time.localtime()
print(time.localtime(1536983039))
print(time.localtime(1536983039))
print(time.mktime(time.localtime()))

# 6.asctime（tuple） 将时间元组转换成字符串
t=time.localtime()
print(time.asctime(t))

# 7.time.sleep(s) 使得当前程序暂停s秒，注意，包含cpu执行的时间，所以不到1s
# time.sleep(1)
# print("dddd")

# 8.clock() :
"""
linux、unix返回cpu的计算时间
windows 函数第一次调用，返回的是cpu的计算时间，从第二次调用开始，返回的是距离第一次调用
        所经历的时间
"""
# print(time.clock())
# time.sleep(1)
# print(time.clock())
# time.sleep(1)
# print(time.clock())

# 9.返回精准的性能计数器，时间包含调用sleep函数暂停的时间
# start=time.perf_counter()
# time.sleep(1)
# end=time.perf_counter()
# print(end-start)

# 10.time.process_time() 返回精准的计数器，不包含sleep函数调用的时间
# start=time.process_time()
# time.sleep(1)
# end=time.process_time()
# print(end-start)


#11. time.strftime(format,元组): 将时间元组转换成字符串
t=time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S",t))

# 12 time.strptime(str，format)：将字符串转换成时间元组
# 要求str必须符合format格式的标准，否则无法转换成元组，报错
print(time.strptime("2018-09-15 12:00:02","%Y-%m-%d %H:%M:%S"))
print(time.strptime("2018-09/15 12:00:02","%Y-%m/%d %H:%M:%S"))



#二、datetime
# 分为三个类：time  date  datetime
from datetime import date
# (一)date类
#1. 构造器: 就是类名.__init__方法。（因为init方法是初始化实例属性的方法。）
# date(year,month,day) :用来创建参数指定日期类型对象
print(date(2018,10,12)) #2018-10-12 是因为在date类下重写str方法
d1=date(2018,10,12)
print(type(d1))

#2. 实例属性
# year
print(d1.year)
# month
print(d1.month)
# day
print(d1.day)
# d1.day=55  #propery之后，只提供了get方法，是只读的
# 相当于date下是这样设计的
# class date:
#     def __init(self,year,month,day):
#         self.__year=year
#         self.__month=month
#         self.__day=day
#     def getyear(self):
#         return self.__year
#     year=property(getyear)

#3. 类属性
# max :最大的对象  9999-12-31
print(date.max)
# min：最小  0000-01-01
print(date.min)
# resolution: 两个对象之间最小的间隔
print(date.resolution)

# 4.实例方法
d1=date(2018,10,12)
# （1）d1.ctime() 返回特定格式的字符串来表示对象的日期
print(d1.ctime())

# (2)d1.replace(year=年，month=月，day=日)，不是原地修改，新创建日期进行修改
d1.replace(month=9)
print(d1.replace(month=9))
print(d1.replace(day=9))

# (3) 可以返回对象的时间元组
# 类似于time.localtime()  不写参数返回当前时间
print(d1.timetuple() ) # 返回当前对象的时间 元组

# (4)d1.weekday()返回当前的日期对象是星期几  （0-6）0是星期一 6是星期日
print(d1.weekday())

# (5)返回当前日期的序数：0001年1月1日  序数1
print(d1.toordinal())

# (6)d1.strftime(format)  将日期类型的对象格式化成字符串
print(d1.strftime("%Y-%m-%d"))
print(d1,type(d1))
a=d1.strftime("%Y-%m-%d")
print(a,type(a))


# 5. 类方法： 返回date类型的对象
# （1）date.today()# 返回当前日期的date对象。
print(date.today())
#（2）date.fromtimestamp(时间戳)  时间戳：从新纪元时间走过的秒数
print(date.fromtimestamp(0))
# (3)date.fromordinal(ordinal)  根据指定的ordinal参数返回date对象
print(date.fromordinal(1))


# （二）time类
# 针对时间的操作
from datetime import time
# 1.构造器
# time(hour,minute,second,microscond) microscond是有默认值0
t=time(3,4,5)
print(t)

#2.实例属性
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)
# t.hour=11

#3. 类属性
# max  min  resolution
print(time.max)  # 23:59:59 999999
print(time.min)
print(time.resolution) # 1微秒

# 4.实例方法
t=time(3,4,5)
#（1）t.replace(hour=,minute=,second=,micorsecond=)
print(t.replace(minute=50))

#(2) t.strftime()将time类型的数据转换成字符串
s=t.strftime("%H:%M:%S")
print(s,type(s))
print(t,type(t))

# （三）.datetime类
# 针对日期和时间的操作，date和time两个功能并集
# 1.构造器
from datetime import datetime
# datetime(年，月，日，时，分，秒，微妙=0)
print(datetime(2018,10,1,1,1,1))

# 2.实例属性
dt=datetime(2018,10,1,1,1,1)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)

#3.类属性
# max
print(datetime.max)
#min
print(datetime.min)
# resolution
print(datetime.resolution)  #1微秒

#4. 实例方法
dt=datetime(2018,10,1,1,1,1)
# （1）dt.date() 将datetime类型的对象，返回一个date类型的对象。
d=dt.date()
print(d,type(d))
# (2) dt.time() 将datetime类型的对象，返回一个time类型的对象。
t=dt.time()
print(t,type(t))
# (3)ctime（）返回特定格式的字符串
print(dt.ctime())

#(4) dt.replace(year=,month=,day=,hour=,minute=,second=,microsecond=)
print(dt.replace(second=24))

#(5) dt.timetuple() 将当前对象转换成时间元组
print(dt.timetuple())

# (6) dt.weekday()，返回当前日期对象的星期几
print(dt.weekday())

# (7)dt.toordinal() 返回当前datetime对象的时间序数
print(dt.toordinal())

#（8）dt.strftime(fmt) 将datetime类型的对象转换成字符串
print(dt.strftime("%Y-%m-%d %H:%M:%S"))

#(9)dt.strptime(fmt)  将字符串转换成datetime类型的对象
print(dt.strptime("2018-10-01 01:01:01","%Y-%m-%d %H:%M:%S"))

# 5.类方法
# （1）datetime.today() 返回当前日期的datetime
print(datetime.today())
# (2) datetime.fromtimestamp(时间戳) 根据指定时间戳返回datetime类型的对象
# print(datetime.fromtimestamp(3600*24))# 只支持1天以上的
# print(datetime.fromtimestamp(3600*26))
#（3）datetime.fromordinal(ord) 根据参数返回datetime类型对象
# print(datetime.fromordinal(1))
# (4)print(datetime.now()返回当前日期的datetime，同today
print(datetime.now())
# （5）datetime.utcfromtimestamp()
#  从1970-1-1，经历了参数指定的时间戳，创建datetime（utc的对象）
print(datetime.utcfromtimestamp(1))

# (6)datetime.strptime(str,fmt) # 将字符串转换成datetime类型的对象
dt1=datetime.strptime("2018-10-01 01:01:01","%Y-%m-%d %H:%M:%S")
print(dt1,type(dt1))




# 三、calendar日历包
import calendar
print(calendar.month(2016,1))
print(calendar.calendar(2018))




