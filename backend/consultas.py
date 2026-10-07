from conexion import Conexion
import sqlite3


def formato(respuesta):
    lista_final = []
    for fila in respuesta.fetchall():
        lista_final.append(dict(fila))
    return lista_final


def select_by_id_omdb(id_omdb: str):
    conexionSelectBy = Conexion(f"SELECT * FROM comment WHERE id_omdb='{id_omdb}';")
    respuesta = conexionSelectBy.res
    resp = formato(respuesta)
    conexionSelectBy.con.close()
    return resp


def insert_data(data):
    try:
        conexionInsert = Conexion(
            'INSERT INTO comment(id_omdb,nombre,comment,fecha) VALUES (?,?,?,?);',
            data,
        )
        conexionInsert.res
        conexionInsert.con.commit()
    except sqlite3.Error as error:
        print('Error: ',error)

    conexionInsert.con.close()