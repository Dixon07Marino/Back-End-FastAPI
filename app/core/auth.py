import jwt, os
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta

#Cargar secretkey
load_dotenv()

#Importar secretkey
SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise Exception(f"Falta secret key")

#Generar token
def generate_token(id_user: int) -> str:
    payload = {
        "id": id_user,
        "exp": datetime.now(timezone.utc) + timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise Exception("Token expirado")
    except jwt.InvalidTokenError:
        raise Exception("Token inválido")


