from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["my_database"]
users = db["users_collection"]

# Insert documents
users.insert_many([
    {"name": "Alice", "age": 30, "salary": 55000, "skills": ["Python", "AI"]},
    {"name": "Bob", "age": 28, "salary": 48000, "skills": ["SQL", "Excel"]},
    {"name": "Charlie", "age": 35, "salary": 62000, "skills": ["Management"]}
])

# Read
print("\nAll Users:")
for user in users.find():
    print(user)

# Update
users.update_one({"name": "Alice"}, {"$set": {"salary": 70000}})
print("\nAfter Salary Update:")
print(users.find_one({"name": "Alice"}))

# Delete
users.delete_one({"name": "Bob"})
print("\nAfter Deleting Bob:")
for user in users.find():
    print(user)
