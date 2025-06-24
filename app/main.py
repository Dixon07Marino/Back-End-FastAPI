from fastapi import FastAPI
from app.api import auth
from app.api import users_crud

#Instancia de FastAPI
app = FastAPI(title="Back-End - FastAPI",
            version="1.0.0",
            summary="API con sistema de Auth y JWT, además cifrado de contraseña - CRUD de Usuarios (Sin create)")

app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(users_crud.router, prefix="/api", tags=["Users"])