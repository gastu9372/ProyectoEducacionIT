from datetime import datetime
from menu import MENU_ITEMS
from encargados import EMPLEADOS
ITEMS = {item.id: item for item in MENU_ITEMS}
ENCARGADOS = {empleado.nombre.lower(): empleado for empleado in EMPLEADOS} # Creamos

opciones = {'1','2','3'} # Opciones validas que tiene el encargado una vez que ingresa en el sistema

def validar_encargado():
    fecha = datetime.now().strftime("%a %b %d %H:%M:%S %Y")  
    while True:
        encargado = input('Ingrese su nombre: ')
        if encargado.lower() in ENCARGADOS:
            linea = f"IN {fecha} ENCARGADO: {encargado}\n"
            # Abrimos el archivo en modo append para no borrar lo anterior
            with open("registro.txt", "a", encoding="utf-8") as f:
                f.write(linea)
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


def nuevo_pedido():
    cliente = nombre_cliente()
    pedido = {}
    total = 0
    print(cliente)
    while True:
        codigo = input('Seleccionar el codigo de item a agregar...: ')
        if codigo in ITEMS:
            cant = input('Ingresar cantidad de este producto: ')
            precio_item = ITEMS[codigo].precio
            total += precio_item * cant
            ITEMS = {item.id: item for item in MENU_ITEMS}


def guardar_venta(cliente, pedido, total):
    fecha = datetime.now().strftime("%a %b %d %H:%M:%S %Y")  
    # Obtenemos las cantidades de cada item (si no está, es 0)
    combo_s = pedido.get("S", 0)
    combo_d = pedido.get("D", 0)
    combo_t = pedido.get("T", 0)
    flurby  = pedido.get("F", 0)

    # Creamos la línea de la venta
    linea = f"{cliente};{fecha};{combo_s};{combo_d};{combo_t};{flurby};${total}\n"

    # Abrimos el archivo en modo append para no borrar lo anterior
    with open("ventas.txt", "a", encoding="utf-8") as f:
        f.write(linea)


def pedir_si_no(msg="¿Desea continuar? (s/n): "):
    while True:
        r = input(msg).strip().lower()
        if r in ("s", "n"):
            return r == "s"
        print("Opción inválida. Ingrese 's' para sí o 'n' para no.")


def pedir_cantidad(msg="Ingresar cantidad de este producto: "):
    while True:
        try:
            cant = int(input(msg))
            if cant > 0:
                return cant
            print("La cantidad debe ser un entero positivo.")
        except ValueError:
            print("Debe ingresar un número válido (entero).")

def pedir_codigo():
    while True:
        codigo = input('Seleccionar el código de item a agregar (S/D/T/F): ').strip().upper()
        if codigo in ITEMS:
            return codigo
        print("Código inválido. Intente nuevamente (S/D/T/F).")


def nuevo_pedido():
    cliente = nombre_cliente()
    pedido = {}
    total = 0
    print(f"Cliente: {cliente}")

    while True:
        # pedir código válido
        codigo = pedir_codigo()
        # pedir cantidad válida
        cant = pedir_cantidad()
        # actualizar totales
        item = ITEMS[codigo]
        total += item.precio * cant
        pedido[codigo] = pedido.get(codigo, 0) + cant

        print(f"Agregado {cant}x {item.nombre} (${item.precio} c/u)")
        print(f"Subtotal: ${total}")

        # preguntar si sigue
        if not pedir_si_no("¿Desea agregar otro item? (s/n): "):
            break

    print(f"\nPedido de {cliente}: {pedido}")
    print(f"Total a pagar: ${total}")
    guardar_venta(cliente, pedido, total)


# Funcion que contiene a las demas funciones y funciona como contenedora
def inicio():
    encargado = validar_encargado() # Primero verificamos encargardo sea valido
    while True:
        print(f'Encargado: {encargado}')
        opcion = elegir_opcion() # Pedimos que seleccione que hara
        if opcion == '1': # Nuevo pedido
            nuevo_pedido()
        elif opcion == '2': # Cambio de turno, se vuelve a validar el empleado y se debe repetir el ciclo 
            fecha = datetime.now().strftime("%a %b %d %H:%M:%S %Y")  
            linea = f"OUT {fecha} ENCARGADO: {encargado}\n"
            with open("registro.txt", "a", encoding="utf-8") as f:
                f.write(linea)
            encargado = validar_encargado()
        elif opcion == '3': # Corta la secuencia
            print('Apagando...')
            fecha = datetime.now().strftime("%a %b %d %H:%M:%S %Y")  
            linea = f"OUT {fecha} ENCARGADO: {encargado}\n"
            with open("registro.txt", "a", encoding="utf-8") as f:
                f.write(linea)
            break
        else: 
            print('Opcion invalida, vuelva a ingresar')


