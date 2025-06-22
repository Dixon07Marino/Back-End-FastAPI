from fastapi import FastAPI
from app.api import auth

#Instancia de FastAPI
app = FastAPI(title="Back-End - FastAPI",
            version="1.0.0",
            summary="API con sistema de Auth y JWT, además cifrado de contraseña")

app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])