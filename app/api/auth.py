from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer
from app.models.user import UserRegister, UserLogin, MessageResponse, TokenResponse
from app.services.auth_service import register_user_service, login_user_service, validate_token_service

router = APIRouter()

#Instancia para validar y extraer token
auth_token = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

#Ruta para registrar user
@router.post("/register", response_model=MessageResponse)
async def register(user: UserRegister):
    return register_user_service(user)
    
#Ruta para loguear user
@router.post("/login", response_model=TokenResponse)
async def login(user: UserLogin):
    return login_user_service(user)

#Ruta protegida para usar el token
@router.get("/protected", response_model=MessageResponse)
async def protected(token: str = Depends(auth_token)):
    return validate_token_service(token)