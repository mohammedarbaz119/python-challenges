from pymongo import MongoClient

db = MongoClient('mongodb://localhost:27017/arbaz')
newcol = db['arbaz']
a = newcol.new.find()
print(list(a))