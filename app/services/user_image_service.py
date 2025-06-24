from fastapi import HTTPException
import os

def get_img(id_img: int) -> str:
    #Permitir mas extensiones
    exts = ["png", "jpeg", "jpg"]
    
    for ext in exts:    
        img_path = f"static_files/images/{id_img}.{ext}"
        if os.path.isfile(img_path):
            return img_path       
    raise HTTPException(status_code=404, detail="Imagen no encontrada")
    
    
