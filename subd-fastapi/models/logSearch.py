from pydantic import BaseModel
import datetime

class Search(BaseModel):
    IP_address: str
    product: str
    dateT: datetime.datetime