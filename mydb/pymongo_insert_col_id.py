# 加载依赖
import pymongo

# 创建连接
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# 定位到数据库mongo_python和集合sites

mp = myclient["mongo_python"]

sites = mp["site2"]
#alexa--->网站的全球排名指标

documents = [
  { "_id": 1, "name": "pyton", "cn_name": "python教程"},
  { "_id": 2, "name": "Google", "address": "Google 搜索"},
  { "_id": 3, "name": "Facebook", "address": "脸书"},
  { "_id": 4, "name": "Taobao", "address": "淘宝"},
  { "_id": 5, "name": "Zhihu", "address": "知乎"}
]

ret = sites.insert_many(documents)

print(ret)
print("-------------$@@$-------------")
##打印插入的文档的id值
print(ret.inserted_ids)





