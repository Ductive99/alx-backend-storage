#!/usr/bin/env python3
"""
Module that defines script that provides stats
about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    """Main Entry"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx = client.logs.nginx

    print("{} logs".format(nginx.count_documents({})))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        requests = nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {requests}")

    status_checks = nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_checks} status check")
