from datetime import datetime
from bbddmanager import DBManager

class Registro:
    def __init__(self, encargado, evento, caja=0):
        self.encargado = encargado
        self.evento = evento  # "IN" o "OUT"
        self.fecha = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
        self.caja = caja

    def guardar_en_db(self, db: DBManager):
        db.insertar(
            "INSERT INTO registro (encargado, fecha, evento, caja) VALUES (?, ?, ?, ?)",
            (self.encargado, self.fecha, self.evento, self.caja)
        )