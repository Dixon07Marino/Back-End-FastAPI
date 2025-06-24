from fastapi import HTTPException
import os

def get_img(id_img: int):
    img_path = f"static_files/images/{id_img}.png"

    if not os.path.isfile(img_path):
        raise HTTPException(status_code=404, detail="Imagen no encontrada")
    
    return img_path
