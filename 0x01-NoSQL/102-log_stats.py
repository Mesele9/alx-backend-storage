#!/usr/bin/env python3
""" log stats """
from pymongo import MongoClient


# connect to mongodb
client = MongoClient('mongodb://localhost:27017')

# select the database
db = client.logs
collection = db.nginx

# count the total number of logs
total_logs = collection.count_documents({})

# print the total number of log
print("{} logs".format(total_logs))

# count the number of document for each method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
print("Methods:")
for method in methods:
    count = collection.count_documents({"method": method})
    print("    method {}: {}".format(method, count))

# count the number of document with method=GET and path=/status
status_check = collection.count_documents({"method": "GET", "path": "/status"})
print("{} status check".format(status_check))

# get the top 10 present IPs
top_ips = collection.aggregate([
    {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 10}
    ])

print("IPs:")
for ip in top_ips:
    print("    {}: {}".format(ip["_id"], ip["count"]))

