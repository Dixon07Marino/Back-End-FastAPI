from fastapi import HTTPException
from app.core.security import hash_password
from app.models.user import UserEmail

def validate_user_existance(data):
    if not data:
        raise HTTPException(status_code=404, detail="El Usuario no existe")
    return data

def extract_data_to_update(id_user: int, data: dict):

    if not data:
        raise HTTPException(status_code=400, detail="No hay datos para actualizar")

    fields = []
    values = []

    if "email" in data:
        # Validar formato de email | Se encarga pydantic
        UserEmail(email=data["email"])

        fields.append("email = %s")
        values.append(data["email"])

    if "password" in data:
        fields.append("password = %s")
        hashed_pwd = hash_password(data["password"])
        values.append(hashed_pwd)

    values.append(id_user)
    return fields, values