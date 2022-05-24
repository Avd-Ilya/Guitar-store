
from models.user import User 
from config.db import database 
from schemas.user import serializeDict, serializeList
from bson import ObjectId
from fastapi import APIRouter, Body, Path, Query, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


user = APIRouter(prefix='/user', tags=["user"]) 


collection = database.user


@user.get('/')
async def find_all_users():
    return serializeList(collection.find())

@user.get('/{id}')
async def find_one_user(id):
    return serializeDict(collection.find_one({"_id":ObjectId(id)}))

@user.post('/new')
async def create_user(user: User):
    collection.insert_one(dict(user))
    return serializeList(collection.find())


@user.put("/edit")
async def update_user(id,user: User):
    collection.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return serializeDict(collection.find_one({"_id":ObjectId(id)}))

@user.delete("/delete")
async def delete_user(id):
    return serializeDict(collection.find_one_and_delete({"_id":ObjectId(id)}))

