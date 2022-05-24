from fastapi import APIRouter
from models.logProduct import Product 
from config.db import database 
from schemas.user import serializeDict, serializeList
from bson import ObjectId
from enum import Enum
from typing import List
import pydantic
from bson import ObjectId, json_util
from fastapi import APIRouter, Body, Path, Query, Response, status
# from fastapi.encoders import jsonable_encoder
# from fastapi.responses import JSONResponse
# from collections import Counter



pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str


logProduct = APIRouter(prefix='/logProduct', tags=["logProduct"]) 


collection = database.logProduct



@logProduct.get('/')
async def find_all_logProduct():
    return serializeList(collection.find())

@logProduct.get('/{id}')
async def find_one_logProduct(id):
    return serializeDict(collection.find_one({"_id":ObjectId(id)}))

@logProduct.post("/new")
async def create_logProduct(Product: Product):
    collection.insert_one(dict(Product))
    return serializeList(collection.find())


@logProduct.put("/edit")
async def update_logProduct(id,Product: Product):
    collection.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(Product)
    })
    return serializeDict(collection.find_one({"_id":ObjectId(id)}))

@logProduct.delete("/delete")
async def delete_logProduct(id, Product: Product):
    return serializeDict(collection.find_one_and_delete({"_id":ObjectId(id)}))


# Вывести самый просматриваемый товар недели 
# @logProduct.get("/")
# async def query1_logProduct():
# 	now=datetime.datetime.now()
# 	startWeek=now-604800000 
# 	# resultArr={}
# 	return serializeDict(collection.find({"dateT":{"$gte":startWeek}}))
	# list1 = collection.find([
	# 	{"$match": {"operation": "view", "dateT": {"$gte": startWeek}}},
	# 	{"$group": {
	# 		"Requested_URL":{
	# 		"count": {"$sum":1}
	# 		}}}])


