import sqlite3

class Conexion:
    def __init__(self, sql_query, parametro=[]):
        self.con = sqlite3.connect("comments_db.db")
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
        self.res = self.cur.execute(sql_query, parametro)