# 1.加载依赖
import pymysql

# 2.打开数据库连接
db=pymysql.connect("localhost","root","123456","homewokr1")

# 3.使用cursor（）方法创建一个游标对象
cursor= db.cursor()

# 4使用execute（） 方法执行sql查询
sql="""

"""
cursor.execute("sql")

# 5.使用fetchone（）方法获取单条数据,获取结果集，并进行封装
data= cursor.fetchone()

# 打印版本号
print("Database version : %s " % data)

# 6.关闭数据库连接
db.close()


