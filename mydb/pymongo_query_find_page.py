# 加载依赖
import pymongo

# 创建连接
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# 定位到数据库mongo_python和集合sites
##use mongo_python
mp = myclient["mongo_python"]

sites = mp["sites"]
##分页显示 skip((2-1)*2).limit(2)
page = 2
limits = 2
siteList = sites.find({}, {"_id": 0, "name": 1, "alexa": 1}).skip((page - 1) * limits).limit(limits)

for site in siteList:
	print(site)
