from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import auth ,users_crud, users_images

#Instancia de FastAPI
app = FastAPI(title="Back-End - FastAPI",
            version="1.0.0",
            summary="API con sistema de Auth y JWT, además cifrado de contraseña - CRUD de Usuarios (Sin create)")

app.mount("/static_files", StaticFiles(directory="static_files"), name="images")

app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(users_crud.router, prefix="/api", tags=["Users"])
app.include_router(users_images.router, prefix="/api/images", tags=["UsersImages"])
