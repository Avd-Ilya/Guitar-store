from pydantic import BaseModel
import datetime

class Product(BaseModel):
	IP_address:str # айпи адрес пользователя 
	Requested_URL: str # товар
	operation: str #view/buy, просто просмотрел или купил
	dateT: datetime.datetime # дата посещения или покупки






