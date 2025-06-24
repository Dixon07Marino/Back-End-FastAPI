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
def get_user_by_email(email: str) -> dict:
    try:
        with connect_db() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id, password FROM Usuarios WHERE email = %s", (email,))
                return cursor.fetchone()
    except Exception as e:
        raise Exception(f"Error, el usuario no existe: {e}")

#Obtener todos los Usuarios
def get_all_users() -> dict:
    try:    
        with connect_db() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM Usuarios")
                return cursor.fetchall()
    except Exception as e:
        raise Exception(f"No hay usuarios disponibles: {e}")

#Obtener usuario por id
def get_user_by_id(id_user: int) -> dict:
    try:
        with connect_db() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM Usuarios WHERE id = %s", (id_user,))
                return cursor.fetchone()
    except Exception as e:
        raise Exception(f"Error interno en la bd: {e}")

#Actualizar usuario por id
def update_user_by_id(fields: list, values: list) -> dict:
    try:
        with connect_db() as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"UPDATE Usuarios SET {', '.join(fields)} WHERE id = %s", tuple(values))
                conn.commit()
                if cursor.rowcount == 0:
                    return {"err": "No se actualizaron datos, el usuario no existe"}
                return {"msg": "Usuario actualizado con exito"}
    except Exception as e:
        raise Exception(f"Error interno en la bd: {e}")

#Eliminar usuario por id
def delete_user_by_id(id_user: int) -> dict:
    try:
        with connect_db() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM Usuarios WHERE id = %s", (id_user,))
                conn.commit()
                if cursor.rowcount == 0:
                    return {"err": "No se eliminaron datos, el usuario no existe"}
                return {"msg": "Usuario eliminado con exito"}
    except Exception as e:
        raise Exception(f"Error interno en la bd: {e}")