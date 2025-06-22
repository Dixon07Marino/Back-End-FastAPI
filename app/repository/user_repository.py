from app.db.connection import connect_db

#Registrar un usuario en la bd
def insert_user(email: str, password: str) -> dict:
    try:
        with connect_db() as conn:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO Usuarios (email, password) VALUES (%s, %s)", (email, password))
                conn.commit()
                return {"msg": "Usuario registrado exitosamente"}
    except Exception as e:
        return {"err": f"Error al registrar usuario: {e}"}
    
#Obtener usuario para el inicio de sesion
def get_user_by_email(email: str):
    try:
        with connect_db() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id, password FROM Usuarios WHERE email = %s", (email,))
                user = cursor.fetchone()
                return user
    except Exception as e:
        raise Exception(f"Error, el usuario no existe: {e}")