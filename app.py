from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from db import register_user, get_user
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
import os, jwt

#Instancia de FastAPI
app = FastAPI(title="Back-End - FastAPI", version="1.0.0", summary="API con sistema de Auth y JWT, además cifrado de contraseña")

#Instancia para cifrar password
pwd_context = CryptContext(schemes="bcrypt", deprecated="auto")

#Cargar secretkey
load_dotenv()

#Importar secretkey
SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise Exception(f"Falta secret key")

#Generar token
def generate_token(id_user: int) -> str:
    payload = {
        "id": id_user,
        "exp": datetime.now(timezone.utc) + timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

#Instancia para validar y extraer token
auth_token = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

#Modelos para validacion de datos
class UserRegister(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

#Ruta para registrar user
@app.post("/api/auth/register")
async def register(user_data: UserRegister):
    try:
        #Cifrar password
        hashed_pwd = pwd_context.hash(user_data.password)
        msg = register_user(user_data.email, hashed_pwd)
        if "err" in msg:
            raise HTTPException(status_code=400, detail=msg.get("err"))
        return msg
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno al registrar usuario: {e}")
    
#Ruta para loguear user
@app.post("/api/auth/login")
async def login(user_data: UserLogin):
    try:
        data = get_user(user_data.email)
        if not data:
            raise HTTPException(status_code=404, detail="El usuario no existe")
        id_user = data.get("id")
        hashed_pwd = data.get("password")
        if not pwd_context.verify(user_data.password, hashed_pwd):
            raise HTTPException(status_code=401, detail="Password invalida")
        token = generate_token(id_user)
        return {"msg": "Has iniciado sesion exitosamente", "token": token}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno al iniciar sesion: {e}")

#Ruta protegida para usar el token
@app.get("/api/auth/protected")
async def protected(token: str = Depends(auth_token)):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms="HS256")
        id_user = decoded.get("id")
        if id_user is None:
            raise HTTPException(status_code=404, detail="Usuario no existe")
        return {"msg": f"El usuario con id: {id_user}, tiene acceso a la app"}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="El token ha expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="El token es invalido")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno al validar token: {e}")