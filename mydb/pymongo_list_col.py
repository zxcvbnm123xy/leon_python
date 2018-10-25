## 加载python和mongo的依赖
import pymongo

## 打开数据库连接 pymongo中操作的对象MongoClient
myclient = pymongo.MongoClient("mongodb://localhost:27017/")


# dbNames = myclient.list_database_names()
mydb = myclient["test"]

cols = mydb.list_collection_names()
##遍历数据库中的所有的列表
for col in cols:
	print(col)
##判断一个集合是否存在于一个数据中
print("////////////////^_^/////////////////////////")
col = "dbs"
if col in cols:
	print("集合", col, "存在于数据库", cols, "中")
else:
	print("数据库", cols, "不包含集合", col)
	
	