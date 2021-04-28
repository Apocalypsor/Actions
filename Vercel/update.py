import pymongo
import sys
import os

project = sys.argv[1]
version = sys.argv[2]
database_url = os.environ["DATABASE"]

client = pymongo.MongoClient(database_url)
db = client["Github"]["Vercel"]

if db.find_one({"project": project}):
    db.update_one({"project": project}, {"$set": {"Ver": version}})
else:
    pro = {"project": project, "Ver": version}
    db.insert_one(pro)
