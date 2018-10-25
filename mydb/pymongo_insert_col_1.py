# 加载依赖
import pymongo

# 创建连接
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# 定位到数据库mongo_python和集合sites

mp = myclient["mongo_python"]

sites = mp["sites"]
#alexa--->网站的全球排名指标

document = {"name": "python", "alexa": "10000", "url": "https://www.python.com"}

ret = sites.insert_one(document)

print(ret)

##打印插入的文档的id值





