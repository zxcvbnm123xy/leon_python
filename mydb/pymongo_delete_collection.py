# 加载依赖
import pymongo

# 创建连接
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# 定位到数据库mongo_python和集合sites
##use mongo_pythonh
mp = myclient["mongo_python"]

cols = mp.list_collection_names()
print("删除之前的集合列表：")
for col in cols:
	print(col)
site2 = mp["site2"]
##删除site2集合

site2.drop()

print("删除之后的集合列表：")
cols = mp.list_collection_names()
for col in cols:
	print(col)