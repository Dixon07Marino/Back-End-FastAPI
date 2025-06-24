from fastapi import APIRouter
from app.repository.user_repository import get_all_users, get_user_by_id, update_user_by_id, delete_user_by_id
from app.services.user_crud_service import validate_user_existance, extract_data_to_update

router = APIRouter()

@router.get("/users")
async def get_users():
    return get_all_users()

@router.get("/user/{id_user}")
async def get_user_id(id_user: int):
    response = get_user_by_id(id_user)
    return validate_user_existance(response)

@router.put("/user/{id_user}")
async def update_user_id(id_user: int, data: dict):
    fields, values = extract_data_to_update(id_user, data)
    return update_user_by_id(fields, values)

@router.delete("/user/{id_user}")
async def delete_user_id(id_user: int):
    return delete_user_by_id(id_user)