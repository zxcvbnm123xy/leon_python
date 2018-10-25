# 加载依赖
import pymongo

# 创建连接
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# 定位到数据库mongo_python和集合sites

mp = myclient["mongo_python"]

sites = mp["sites"]
#alexa--->网站的全球排名指标

documents = [
  { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
  { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
  { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
  { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
  { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
]

ret = sites.insert_many(documents)

print(ret)

##打印插入的文档的id值





