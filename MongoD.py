import pymongo

client = pymongo.MongoClient("localhost", 27017)
print(client)

db = client.testmongo
collection = db.test_coll

print(db.name)
print(db.test_coll)

