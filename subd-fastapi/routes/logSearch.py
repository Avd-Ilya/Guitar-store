from fastapi import APIRouter
from models.logSearch import Search 
from config.db import database 
from schemas.user import serializeDict, serializeList
from bson import ObjectId
import pydantic
from fastapi import APIRouter


pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str
logSearch = APIRouter(prefix='/logSearch', tags=["logSearch"]) 
collection = database.logSearch



@logSearch.get('/')
async def find_all_logSearch():
    return serializeList(collection.find())

@logSearch.get('/{id}')
async def find_one_logSearch(id):
    return serializeDict(collection.find_one({"_id":ObjectId(id)}))

@logSearch.post("/new")
async def create_logSearch(Search: Search):
    collection.insert_one(dict(Search))
    return serializeList(collection.find())


@logSearch.put("/edit")
async def update_logSearch(id,Search: Search):
    collection.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(Search)
    })
    return serializeDict(collection.find_one({"_id":ObjectId(id)}))

@logSearch.delete("/delete")
async def delete_logSearch(id):
    return serializeDict(collection.find_one_and_delete({"_id":ObjectId(id)}))

# 5 популярных поисковых запросов
@logSearch.post("/query")
async def query_logSearch(): 
	result = collection.aggregate([
    { "$group": {
        "_id": {
            "product": "$product",
        },
        "count": { "$sum": 1 }
    }},
		{"$sort": { "count": -1 }},
		{"$limit" : 5}
])
	return serializeList(result)



