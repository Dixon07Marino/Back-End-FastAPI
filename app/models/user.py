from pydantic import BaseModel, EmailStr

#Modelos para validacion de datos
class UserRegister(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class MessageResponse(BaseModel):
    msg: str

class TokenResponse(BaseModel):
    msg: str
    token: str