from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    username:str
    
    @field_validator('username')
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username is not valid, it must be at least 4 chars")
        return v

class SignupData(BaseModel):
    password: str
    confirm_password: str
    
    @model_validator(mode= 'after')
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("password doesnot Match, Please do the thing once again")
        return values