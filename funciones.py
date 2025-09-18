from menu import MENU_ITEMS
from encargados import EMPLEADOS
ITEMS = {item.id: item for item in MENU_ITEMS}
ENCARGADOS = {empleado.nombre.lower(): empleado for empleado in EMPLEADOS} # Creamos

opciones = {'1','2','3'} # Opciones validas que tiene el encargado una vez que ingresa en el sistema

def validar_encargado():
    while True:
        encargado = input('Ingrese su nombre: ')
        if encargado.lower() in ENCARGADOS:
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


# def nuevo_pedido():
#     opcion = elegir_opcion()
#     cliente = nombre_cliente()
#     pedido = {}
#     print(opcion, cliente)
    # while True:
    #     codigo = input('Seleccionar el codigo de item a agregar...: ')
    #     if codigo in ITEMS:
    #         cant = input()


# Funcion que contiene a las demas funciones y funciona como contenedora
def inicio():
    encargado = validar_encargado()
    opcion = elegir_opcion()
    while True:
    if opcion == 1:
        break
    elif opcion == 2:
        break
    elif opcion == 3:
        break
    else: 
        print('Opcion invalida, vuelva a ingresar')

inicio()
    
