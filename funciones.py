from menu import MENU_ITEMS

ITEMS = {item.id: item for item in MENU_ITEMS}


opciones = {'1','2','3'}

def elegir_opcion():
    while True:
        opcion = input('1 – Ingreso nuevo pedido\n2 – Cambio de turno\n3 – Apagar sistema\n'  ).strip()
        if not opcion in opciones:
            print('Opcion Invalida. Intenta de nuevo')
        else:
            return opcion

def nombre_cliente():
    while True:
        cliente = input('Ingrese el nombre del cliente: ').strip()
        tiene_digito = any(ch.isdigit() for ch in cliente)
        if cliente and not tiene_digito:
            return cliente
        print('Nombre Invalido. El nombre no puede contener numeros')


def nuevo_pedido():
    opcion = elegir_opcion()
    cliente = nombre_cliente()
    pedido = {}
    print(opcion, cliente)
    # while True:
    #     codigo = input('Seleccionar el codigo de item a agregar...: ')
    #     if codigo in ITEMS:
    #         cant = input()

