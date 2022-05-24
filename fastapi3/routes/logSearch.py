from fastapi import APIRouter
from models.logSearch import Search 
from config.db import database 
from schemas.user import serializeDict, serializeList
from bson import ObjectId
from enum import Enum
from typing import List, Optional

import pydantic
from bson import ObjectId, json_util
from fastapi import APIRouter, Body, Path, Query, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse



pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str


logSearch = APIRouter(prefix='/logSearch', tags=["logSearch"]) 


collection = database.logSearch



@logSearch.get('/', description="Get informations about an users")
async def find_all_logSearch():
    return serializeList(collection.find())

@logSearch.get('/{id}')
async def find_one_logSearch(id):
    return serializeDict(collection.find_one({"_id":ObjectId(id)}))

@logSearch.post("/new", description="Create a new user")
async def create_logSearch(Search: Search):
    collection.insert_one(dict(Search))
    return serializeList(collection.find())


@logSearch.put("/edit", description="Edit an existing user")
async def update_logSearch(id,Search: Search):
    collection.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(Search)
    })
    return serializeDict(collection.find_one({"_id":ObjectId(id)}))

@logSearch.delete("/delete", description="Delete an existing user")
async def delete_logSearch(id, Search: Search):
    return serializeDict(collection.find_one_and_delete({"_id":ObjectId(id)}))



