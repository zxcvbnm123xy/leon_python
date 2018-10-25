# 加载依赖
import pymongo

# 创建连接
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# 定位到数据库mongo_python和集合sites
##use mongo_python
mp = myclient["mongo_python"]

sites = mp["sites"]
##db.sites.find({"alexa": {$gt: "10"}}, {"_id": 0, "name": 1, "alexa": 1})
siteList = sites.find({"alexa": {"$gt": "10"}}, {"_id": 0, "name": 1, "alexa": 1})

for site in siteList:
	print(site)
print("----------------------------------------------------------------------")
siteList = sites.find({"name": {"$gt": "H"}}, {"_id": 0, "name": 1, "alexa": 1})

for site in siteList:
	print(site)
print("----------------------------------------------------------------------")

siteList1 = sites.find({"name": {"$regex": "^[G|g].{2}$"}}, {"_id": 0, "name": 1, "alexa": 1})
for site in siteList1:
	print(site)






