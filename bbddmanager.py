import sqlite3
from datetime import datetime

class DBManager:
    def __init__(self, db_name="comercio.sqlite"):
        self.con = sqlite3.connect(db_name)
        self.crear_tablas()

    def crear_tablas(self):
        cur = self.con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS venta (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente TEXT,
                fecha TEXT,
                ComboS INT,
                ComboD INT,
                ComboT INT,
                Flurby INT,
                total REAL,
                encargado TEXT
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS registro (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                encargado TEXT,
                fecha TEXT,
                evento TEXT,
                caja REAL
            )
        """)
        self.con.commit()

    def insertar(self, query, params):
        cur = self.con.cursor()
        cur.execute(query, params)
        self.con.commit()