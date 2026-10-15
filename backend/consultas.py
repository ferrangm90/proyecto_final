from conexion import Conexion
import sqlite3


def formato(respuesta):
    """
    Pasa la respuesta de la BBDD a una lista de diccionarios
    """
    lista_final = []
    for fila in respuesta.fetchall():
        lista_final.append(dict(fila))
    return lista_final


def select_id_omdb(id_omdb: str):
    """
    Get de los comentarios en la BBDD filtrando por el id de omdb
    """
    conexionSelectBy = Conexion(f"SELECT * FROM comment WHERE id_omdb='{id_omdb}';")
    respuesta = conexionSelectBy.res
    resp = formato(respuesta)
    conexionSelectBy.con.close()
    return resp


def insert_data(data):
    """
    Inserta un comentario en la BBDD
    """
    try:
        conexionInsert = Conexion(
            'INSERT INTO comment(id_omdb,nombre,comment,fecha) VALUES (?,?,?,?);',data)
        conexionInsert.res
        conexionInsert.con.commit()
    except sqlite3.Error as error:
        print('Error: ',error)

    conexionInsert.con.close()


def select_calificaciones_id_omdb(id_omdb: str):
    """
    Obtiene todas las calificaciones de una película por su id_omdb
    """
    conexionSelectBy = Conexion(f"SELECT * FROM calificacion WHERE id_omdb='{id_omdb}';")
    respuesta = conexionSelectBy.res
    resp = formato(respuesta)
    conexionSelectBy.con.close()
    return resp


def insert_calificacion(data):
    """
    Inserta una nueva calificación en la base de datos
    """
    try:
        conexionInsert = Conexion(
            'INSERT INTO calificacion(id_omdb,nombre,calificacion,fecha) VALUES (?,?,?,?);', data)
        conexionInsert.res
        conexionInsert.con.commit()
    except sqlite3.Error as error:
        print('Error: ', error)

    conexionInsert.con.close()


def calcular_promedio(lista_calificaciones):
    """
    Calcula el promedio de calificaciones
    """
    if len(lista_calificaciones) == 0:
        return {"promedio": 0, "total": 0}
    
    suma = 0
    for calificacion in lista_calificaciones:
        suma += calificacion["calificacion"]
    
    promedio = round(suma / len(lista_calificaciones), 1)
    return {"promedio": promedio, "total": len(lista_calificaciones)}