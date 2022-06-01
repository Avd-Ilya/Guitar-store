import bson
from fastapi import APIRouter, Response, status
from models.logProduct import Product 
from config.db import database 
from schemas.user import serializeDict, serializeList
from bson import ObjectId
from enum import Enum
from typing import List
import datetime
import pydantic
from bson import ObjectId, json_util
from fastapi import APIRouter, Body, Path, Query, Response, status

logProduct = APIRouter(prefix='/logProduct', tags=["logProduct"]) 
collection = database.logProduct

@logProduct.get('/')
async def find_all_logProduct():
    return serializeList(collection.find())

@logProduct.get('/{id}')
async def find_one_logProduct(id):
	try:
		return serializeDict(collection.find_one({"_id":ObjectId(id)}))
	except bson.errors.InvalidId:
		return False

@logProduct.post("/new")
async def create_logProduct(Product: Product):
    collection.insert_one(dict(Product))
    return serializeList(collection.find())


@logProduct.put("/edit")
async def update_logProduct(id,Product: Product):
	try:
		collection.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(Product)
    })
		return serializeDict(collection.find_one({"_id":ObjectId(id)}))
	except bson.errors.InvalidId:
		return False

@logProduct.delete("/delete")
async def delete_logProduct(id):
	try:
		return serializeDict(collection.find_one_and_delete({"_id":ObjectId(id)}))
	except bson.errors.InvalidId:
		return False


# Вывести самый просматриваемый товар недели 
@logProduct.post("/query1")
async def query1_logProduct():
	now=datetime.datetime.now()
	week=datetime.timedelta(days=7)
	startWeek=now-week 
	result = collection.aggregate([
    { "$match": { "dateT": { "$gte": startWeek } ,"operation": "view"} },
    { "$group": {
        "_id": {
            "Requested_URL": "$Requested_URL",
        },
        "count": { "$sum": 1 }
    }},
		{"$sort": { "count": -1 }},
		{"$limit" : 1}
])
	return serializeList(result)


# Вывести самый просматриваемый товар месяца 
@logProduct.post("/query2")
async def query2_logProduct():
	now=datetime.datetime.now()
	week=datetime.timedelta(days=30)
	startMonth=now-week 
	result = collection.aggregate([
    { "$match": { "dateT": { "$gte": startMonth } ,"operation": "view"} },
    { "$group": {
        "_id": {
            "Requested_URL": "$Requested_URL",
        },
        "count": { "$sum": 1 }
    }},
		{"$sort": { "count": -1 }},
		{"$limit" : 1}
])
	return serializeList(result)


# Вывести самый покупаемый товар
@logProduct.post("/query3")
async def query3_logProduct(): 
	result = collection.aggregate([
    { "$match": {"operation": "buy"} },
    { "$group": {
        "_id": {
            "Requested_URL": "$Requested_URL",
        },
        "count": { "$sum": 1 }
    }},
		{"$sort": { "count": -1 }},
		{"$limit" : 1}
])
	return serializeList(result)
