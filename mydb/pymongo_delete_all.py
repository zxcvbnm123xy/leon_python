# 加载依赖
import pymongo

# 创建连接
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# 定位到数据库mongo_python和集合sites
##use mongo_python
mp = myclient["mongo_python"]

site2 = mp["site2"]
##删除name以G或者g开头的文档


ret = site2.delete_many({})
print(ret)
print("------------删除之后的数据----------------")

sites = site2.find()
for site in sites:
	print(site)