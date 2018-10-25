## 加载python和mongo的依赖
import pymongo

## 打开数据库连接 pymongo中操作的对象MongoClient
myclient = pymongo.MongoClient("mongodb://localhost:27017/")


# dbNames = myclient.list_database_names()
dbNames = myclient.database_names()

for db in dbNames:
	if "monogs" == db:
		print (db, "存在于mongo数据库中")
	else:
		print(db)