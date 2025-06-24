from fastapi import HTTPException
from app.models.user import UserRegister, UserLogin
from app.repository.user_repository import insert_user, get_user_by_email
from app.core.security import hash_password, verify_password
from app.core.auth import generate_token, decode_token

def register_user_service(user: UserRegister) -> dict:
    hashed_pwd = hash_password(user.password)
    result = insert_user(user.email, hashed_pwd)
    if "err" in result:
        raise HTTPException(status_code=400, detail=result.get("err"))
    return result
  
def login_user_service(user: UserLogin) -> dict:
    data = get_user_by_email(user.email)
    if not data:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    if not verify_password(user.password, data["password"]):
        raise HTTPException(status_code=401, detail="Password invalida")
    token = generate_token(data["id"])
    return {"msg": "Has iniciado sesion exitosamente", "token": token}

def validate_token_service(token: str) -> dict:
    try:     
        payload = decode_token(token)
        user_id = payload.get("id")
        if not user_id:
            raise HTTPException(status_code=404, detail="Usuario no valido")
        return {"msg": f"El usuario con id: {user_id} tiene acceso"}
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"{e}")