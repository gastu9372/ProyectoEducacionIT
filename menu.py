# Creo un objeto menu. Esto es para tener mayor control sobre los items y poder extraer lo que se necesite.
# Tambien sirve para tener codigo reeutilizable y escalable.

class MenuItem:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

# Con esto hacemos que cuando se pida la info del menu se vea prolijo y no como una direccion de memoria
    def __str__(self):
        return f"{self.id} - {self.nombre} ${self.precio}"

     # Para que en dicts/lists se vea lindo
    def __repr__(self):
        return self.__str__()

# Defino los ítems que siempre existen
MENU_ITEMS = [
    MenuItem("S", "Combo Simple", 5),
    MenuItem("D", "Combo Doble", 6),
    MenuItem("T", "Combo Triple", 7),
    MenuItem("F", "McFlurby", 2)
]

