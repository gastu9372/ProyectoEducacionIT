# Este objeto empleado es para en caso de que se necesite infomracion mas alla del nombre

class InfoEmpleado:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    

    def __str__(self):
        return f"{self.dni} - {self.nombre} {self.apellido}"

EMPLADOS = [
    InfoEmpleado('12345678', 'Nahuel', 'Soria'),
    InfoEmpleado('12345679', 'Gonzalo', 'Turati'),
    InfoEmpleado('12345698', 'Luis', 'Castillo'),
    InfoEmpleado('12345688', 'Tomas', 'Canonico'),
]

