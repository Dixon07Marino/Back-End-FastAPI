from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.services.user_image_service import get_img

router = APIRouter()

@router.get("/{id_img}")
async def get_img_user(id_img: int):
    img_path = get_img(id_img)
    return FileResponse(img_path)