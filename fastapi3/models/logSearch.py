from pydantic import BaseModel
import datetime

# популярные поисковые запросы пользователей
class Search(BaseModel):
    IP_address: str
    product: str
    dateT: datetime.datetime