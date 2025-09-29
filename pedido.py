from datetime import datetime
from menu import MENU_ITEMS
from bbddmanager import DBManager
import requests

def consultar_dolar():
    try:
        r = requests.get("https://api.bluelytics.com.ar/v2/latest")
        data = r.json()
        return data["blue"]["value_sell"]  # dólar blue venta
    except Exception:
        return 1000.0  # valor fijo de fallback



ITEMS = {item.id: item for item in MENU_ITEMS}

class Pedido:
    def __init__(self, cliente, encargado):
        self.cliente = cliente
        self.encargado = encargado
        self.fecha = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
        self.items = {}   # {codigo: cantidad}
        self.total = 0

    def agregar_item(self, codigo, cantidad):
        """Agrega un item por código, verificando existencia"""
        if codigo not in ITEMS:
            raise ValueError("Código inválido de producto")
        item = ITEMS[codigo]
        self.items[codigo] = self.items.get(codigo, 0) + cantidad
        valor_dolar = consultar_dolar()
        self.total += item.precio * cantidad * valor_dolar
        print(f"Agregado {cantidad}x {item.nombre} (${item.precio * valor_dolar} c/u)")
        print(f"Subtotal: ${self.total}")

    def mostrar_resumen(self):
        valor_dolar = consultar_dolar()
        print(f"\nPedido de {self.cliente} (Encargado: {self.encargado})")
        for codigo, cantidad in self.items.items():
            item = ITEMS[codigo]
            print(f" - {cantidad}x {item.nombre} (${item.precio * valor_dolar} c/u)")
        print(f"TOTAL: ${self.total}")


    def guardar(self, archivo="ventas.txt"):
        """Persistir el pedido en un archivo CSV-like"""
        combo_s = self.items.get("S", 0)
        combo_d = self.items.get("D", 0)
        combo_t = self.items.get("T", 0)
        flurby  = self.items.get("F", 0)

        linea = f"{self.cliente};{self.fecha};{combo_s};{combo_d};{combo_t};{flurby};${self.total}\n"
        with open(archivo, "a", encoding="utf-8") as f:
            f.write(linea)
    
    def guardar_en_db(self, db: DBManager):
        combo_s = self.items.get("S", 0)
        combo_d = self.items.get("D", 0)
        combo_t = self.items.get("T", 0)
        flurby  = self.items.get("F", 0)

        db.insertar(
            "INSERT INTO venta (cliente, fecha, ComboS, ComboD, ComboT, Flurby, total, encargado) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (self.cliente, self.fecha, combo_s, combo_d, combo_t, flurby, self.total, self.encargado)
        )
