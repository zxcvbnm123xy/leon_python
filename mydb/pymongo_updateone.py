# 加载依赖
import pymongo

# 创建连接
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# 定位到数据库mongo_python和集合sites
##use mongo_python
mp = myclient["mongo_python"]

sites = mp["sites"]

ret = sites.update_one({"alexa": "12345"}, {"$set": {"alexa": "10000"}})

print(ret)
