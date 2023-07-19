#!/usr/bin/env python3
""" log stats """

from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')

db = client.logs
collection = db.nginx

total_logs = collection.count_documents({})

print("{} logs".format(total_logs))

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    count = collection.count_documents({"method": method})
    print("method {}: {}".format(method, count))

status_check = collection.count_documents({"method": "GET", "path": "/status"})
print("{} status check".format(status_check))
