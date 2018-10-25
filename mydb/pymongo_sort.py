# 加载依赖
import pymongo

# 创建连接
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# 定位到数据库mongo_python和集合sites
##use mongo_python
mp = myclient["mongo_python"]

sites = mp["sites"]
#按照alexa降序，name升序  db.sites.find().sort({"alexa": -1, "name": 1})
siteList = sites.find({}, {"_id": 0, "name": 1, "alexa": 1})\
	.sort([("alexa", pymongo.DESCENDING), \
	("name", pymongo.ASCENDING)])

for site in siteList:
	print(site)
