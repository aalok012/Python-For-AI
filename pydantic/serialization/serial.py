from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    street: str
    city:str
    postal_code: str
    
class User(BaseModel):
    id: int
    name:str
    email: str
    is_Active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str]= []
    
    model_config= ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )
    
    
user= User(
    id= 100,
    name="Alok Thakur",
    email= "aalok@gmail.com",
    is_Active= False,
    createdAt= datetime(2025, 4, 1, 14, 30,2),
    address= Address(
    street="Chandani tole",
    city="Inaruwa",
    postal_code= "78666"
    ),
    tags=  ["Premium users", "subscribers"]
)

user1= user.model_dump_json()
print(user1)