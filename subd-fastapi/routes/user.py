
from ctypes.wintypes import PINT
import bson
from models.user import User
from config.db import database 
from schemas.user import serializeDict, serializeList
from bson import ObjectId
from fastapi import APIRouter,  HTTPException



authID = APIRouter(prefix='/user', tags=["user"]) 
collection = database.authID

def verify_password(self, plain_password, hashed_password):
	return self.pwd_context.verify(plain_password, hashed_password)


@authID.get('/')
async def find_all_users():
    return serializeList(collection.find())

@authID.get('/{id}')
async def find_one_user(id):
	try:
		return serializeDict(collection.find_one({"_id":ObjectId(id)}))
	except bson.errors.InvalidId:
		return False

@authID.post('/new')
async def create_user(user: User):
	if collection.find_one({"email":user.email}):
		raise HTTPException(status_code=400, detail='Username is already present')
	else:
		collection.insert_one(dict(user))
		return serializeList(collection.find())


@authID.put("/edit")
async def update_user(id,user: User):
	try:
		collection.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)})
		return serializeDict(collection.find_one({"_id":ObjectId(id)}))
	except bson.errors.InvalidId:
		return False

@authID.delete("/delete")
async def delete_user(id):
	try:
		return serializeDict(collection.find_one_and_delete({"_id":ObjectId(id)}))
	except bson.errors.InvalidId:
		return False

# Авторизация пользователя
@authID.post("/auth/{email},{password}")
async def auth_user(email, password):
	user= None
	getUser=collection.find_one({"email":email})
	if getUser:
		user = getUser
		if (user is None) or (not password == user['password']):
			raise HTTPException(status_code=401, detail='Invalid username and/or password')
		else:
			return serializeDict(getUser)
	else:
		raise HTTPException(status_code=401, detail='Invalid username and/or password')
