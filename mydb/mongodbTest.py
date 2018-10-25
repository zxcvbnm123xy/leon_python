# 加载python和mongo的依赖
import pymongo

# 打开数据库连接 pymongo中操作的对象MongoClient
myclient = pymongo.MongoClient('mongodb://localhost:27017')

# 创建数据库
mydb=myclient["mongo_python"]
# 创建集合
mycol=mydb["sites"]

document=({"name":"python","alexa":"10000","url":"www.baidu.com"})

ret=mycol.insert_one(document)
print(ret)



