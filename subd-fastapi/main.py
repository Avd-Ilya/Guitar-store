# dXV4bByL8M7s3fsa

# client = pymongo.MongoClient("mongodb+srv://test_user:<password>@guitarstore.hnptx.mongodb.net/?retryWrites=true&w=majority")
# db = client.test 
import uvicorn
from fastapi import FastAPI
from routes.user import authID 
from routes.logSearch import logSearch 
from routes.logProduct import logProduct 

app = FastAPI()
app.include_router(authID)
app.include_router(logProduct)
app.include_router(logSearch)

if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)



