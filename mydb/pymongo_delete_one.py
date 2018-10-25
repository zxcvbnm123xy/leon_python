# 加载依赖
import pymongo

# 创建连接
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# 定位到数据库mongo_python和集合sites
##use mongo_python
mp = myclient["mongo_python"]

site2 = mp["site2"]
##删除一条记录

query_condition={"name":"Facebook"}
ret = site2.delete_one(query_condition)
print(ret)