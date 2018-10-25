# 加载依赖
import pymongo

# 创建连接
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# 定位到数据库mongo_python和集合sites
##use mongo_python
mp = myclient["mongo_python"]

sites = mp["sites"]

#db.sites.update({"name": {$regex: "^[G|g]"}}, {$set: {"alexa": "4321"}}, {"multi":true})
query={"name": {"$regex": "^[G|g]"}}
update_value={"$set": {"alexa": "1234"}}
ret = sites.update_many(query, update_value)

print(ret.modified_count, "个文档被修改。")