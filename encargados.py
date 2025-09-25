from datetime import datetime

# Este objeto empleado es para en caso de que se necesite infomracion mas alla del nombre

class InfoEmpleado:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    
# Con esto hacemos que cuando se pida la info de un empleado se vea prolijo y no como una direccion de memoria
    def __str__(self):
        return f"{self.dni} - {self.nombre} {self.apellido}"
    
     # Para que en dicts/lists se vea lindo
    def __repr__(self):
        return self.__str__()



class Encargado:
    def __init__(self, empleado: 'InfoEmpleado'):
        self.empleado = empleado
        self.fecha_login = None
        self.activo = False

    def login(self, db):
        """Marca inicio de turno (evento IN)"""
        self.fecha_login = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
        self.activo = True
        # Guardar en DB (evento IN)
        db.insertar(
            "INSERT INTO registro (encargado, fecha, evento, caja) VALUES (?, ?, ?, ?)",
            (self.empleado.nombre, self.fecha_login, "IN", 0)
        )
        print(f"Encargado {self.empleado.nombre} inició turno.")

    def logout(self, db):
        fecha_logout = datetime.now().strftime("%a %b %d %H:%M:%S %Y")

        cursor = db.con.cursor()
        cursor.execute("""
            SELECT SUM(total) FROM venta
            WHERE encargado = ? AND fecha >= ?
        """, (self.empleado.nombre, self.fecha_login))
        resultado = cursor.fetchone()[0]
        caja = resultado if resultado else 0.0

        db.insertar(
            "INSERT INTO registro (encargado, fecha, evento, caja) VALUES (?, ?, ?, ?)",
            (self.empleado.nombre, fecha_logout, "OUT", caja)
        )
        self.activo = False
        print(f"Encargado {self.empleado.nombre} cerró turno con caja: ${caja}")



EMPLEADOS = [
    InfoEmpleado('12345678', 'Nahuel', 'Soria'),
    InfoEmpleado('12345679', 'Gonzalo', 'Turati'),
    InfoEmpleado('12345698', 'Luis', 'Castillo'),
    InfoEmpleado('12345688', 'Tomas', 'Canonico'),
]

