# db.py
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
main_db = client["myLoginDatabase"]
productDB = client["grocery_store"]

# Collections
users_collection = main_db["users"]
orders_collection = main_db["Orders"]
complaints_collection = main_db["Complaints"]
adminpin = main_db["admins"]
