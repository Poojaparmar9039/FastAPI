from pydantic import BaseModel,EmailStr

class Usercreate(BaseModel):
    name:str
    email:EmailStr
    password:str