from typing import Optional
from pydantic import BaseModel, Field

class Employee(BaseModel):
    id:int
    name: str =Field(
        ...,
        min_length=3, 
        max_length=50,
        description="employee name"
        examples="ALOK THAKUR"
        
    )
    department: Optional[str]= 'General'
    salary: float= Field(
        ...,
        ge=10000,
        le=100000000,
        
    )
class User(BaseModel):
    email: str= Field(...,regex=r"^[a-zA-Z0-9_]{3,15}$" )
    phone: str= Field(..., regex=r"^[a-zA-Z0-9_]{3,15}$")