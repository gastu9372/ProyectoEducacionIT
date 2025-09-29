import requests
from menu import MENU_ITEMS
from encargados import EMPLEADOS, Encargado
from bbddmanager import DBManager
from registro import Registro
from pedido import Pedido
ITEMS = {item.id: item for item in MENU_ITEMS}
ENCARGADOS = {empleado.nombre.lower(): empleado for empleado in EMPLEADOS} # Creamos

opciones = {'1','2','3'} # Opciones validas que tiene el encargado una vez que ingresa en el sistema

def validar_encargado(db):
    while True:
        nombre = input('Ingrese su nombre: ').strip().lower()
        empleado = ENCARGADOS.get(nombre)
        if empleado:
            encargado = Encargado(empleado)
            encargado.login(db)  # Guarda IN en DB
            return encargado
        else:
            print("Error. No se encuentra el encargado, vuelva a ingresar.")


##  Funcion para elegir la opicion
def elegir_opcion():
    while True:
        opcion = input('1 – Ingreso nuevo pedido\n2 – Cambio de turno\n3 – Apagar sistema\n'  ).strip()
        if not opcion in opciones:
            print('Opcion Invalida. Intenta de nuevo')
        else:
            return opcion

##  Funcion para ingresar nombre de cliente
def nombre_cliente():
    while True:
        cliente = input('Ingrese el nombre del cliente: ').strip()
        tiene_digito = any(ch.isdigit() for ch in cliente) # Para verificar que sea un nombre valido
        if cliente and not tiene_digito: # Si es valido devuelve el nombre del cliente
            return cliente
        print('Nombre Invalido. El nombre no puede contener numeros')

# Funcion para ver si se desea continuar
def pedir_si_no(msg="¿Desea continuar? (s/n): "):
    while True:
        r = input(msg).strip().lower()
        if r in ("s", "n"):
            return r == "s"
        print("Opción inválida. Ingrese 's' para sí o 'n' para no.")

# Fucnion para pedir cantidad de prodcuto
def pedir_cantidad(msg="Ingresar cantidad de este producto: "):
    while True:
        try:
            cant = int(input(msg))
            if cant > 0:
                return cant
            print("La cantidad debe ser un entero positivo.")
        except ValueError:
            print("Debe ingresar un número válido (entero).")

# Funcion para pedir el codigo del producto
def pedir_codigo():
    while True:
        codigo = input('Seleccionar el código de item a agregar (S/D/T/F): ').strip().upper()
        if codigo in ITEMS:
            return codigo
        print("Código inválido. Intente nuevamente (S/D/T/F).")

# Funcion para iniciar un nuevo pedido
def nuevo_pedido(encargado):
    cliente = nombre_cliente()
    pedido = Pedido(cliente, encargado)
    print(f"Cliente: {cliente}")

    while True:
        codigo = pedir_codigo()
        cant = pedir_cantidad()
        pedido.agregar_item(codigo, cant)

        if not pedir_si_no("¿Desea agregar otro item? (s/n): "):
            break

    pedido.mostrar_resumen()
    return pedido   # <<--- devolverlo, no guardarlo acá


def guardar_en_db(self, db: DBManager):
    combo_s = self.items.get("S", 0)
    combo_d = self.items.get("D", 0)
    combo_t = self.items.get("T", 0)
    flurby  = self.items.get("F", 0)
    db.insertar(
        "INSERT INTO venta (cliente, fecha, ComboS, ComboD, ComboT, Flurby, total) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (self.cliente, self.fecha, combo_s, combo_d, combo_t, flurby, self.total)
    )




# Funcion que contiene a las demas funciones y funciona como contenedora
def inicio():
    db = DBManager()
    encargado = validar_encargado(db)

    while True:
        print(f'Encargado: {encargado.empleado.nombre}')
        opcion = elegir_opcion()
        
        if opcion == '1':  # Nuevo pedido
            pedido = nuevo_pedido(encargado.empleado.nombre)
            pedido.guardar_en_db(db)

        elif opcion == '2':  # Cambio de turno
            encargado.logout(db)
            encargado = validar_encargado(db)

        elif opcion == '3':  # Apagar sistema
            print('Apagando...')
            encargado.logout(db)
            break



