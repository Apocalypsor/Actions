import pymongo
import sys
import os

project = sys.argv[1]
version = sys.argv[2]
database_url = os.environ["DATABASE"]

client = pymongo.MongoClient(database_url)
db = client["Github"]["Vercel"]

project_data = db.find_one({"project": project})
if project_data:
    if project_data["Ver"] != version:
        print("Updating")
else:
    print("Updating")
