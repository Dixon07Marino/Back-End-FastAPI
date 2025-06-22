import mysql.connector, os
from dotenv import load_dotenv

#Cargar vars de entorno
load_dotenv()

#Validar vars de entorno paraa la conexion
vars_needed = ["DB_HOST", "DB_PASSWORD", "DB_NAME", "DB_USER"]
vars_missing = [var for var in vars_needed if not os.getenv(var)]

if vars_missing:
    raise Exception(f"Faltan vars de entorno: {vars_missing}")

#Crear conexion a la bd con mysql

def connect_db():
    conection = mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        database = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD")
    )
    return conection

#Registrar un usuario en la bd
def register_user(email: str, password: str) -> dict:
    try:
        with connect_db() as conn:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO Usuarios (email, password) VALUES (%s, %s)", (email, password))
                conn.commit()
                return {"msg": "Usuario registrado exitosamente"}
    except Exception as e:
        return {"err": f"Error al registrar usuario: {e}"}
    
#Obtener usuario para el inicio de sesion
def get_user(email: str):
    try:
        with connect_db() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id, password FROM Usuarios WHERE email = %s", (email,))
                user = cursor.fetchone()
                return user
    except Exception as e:
        raise Exception(f"Error, el usuario no existe: {e}")