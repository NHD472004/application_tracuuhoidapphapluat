from pymongo import MongoClient


client = MongoClient("mongodb+srv://admin:admin@cluster0.nn6abqc.mongodb.net/?retryWrites=true&w=majority")
client.admin.command("ping")

db = client.todo_db

collection_name = db["todo_collection"]