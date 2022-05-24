# import motor.motor_asyncio

# client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://test_user:dXV4bByL8M7s3fsa@guitarstore.hnptx.mongodb.net/?retryWrites=true&w=majority')
# database = client.GuitarStore
# collection = database.user

# 2 вариант
from pymongo import MongoClient
conn = MongoClient('mongodb+srv://test_user:dXV4bByL8M7s3fsa@guitarstore.hnptx.mongodb.net/?retryWrites=true&w=majority')
database = conn.GuitarStore

