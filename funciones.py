from menu import MENU_ITEMS
opciones = {'1','2','3'}

def elegir_opcion():
    while True:
        opcion = input('1 – Ingreso nuevo pedido\n2 – Cambio de turno\n3 – Apagar sistema\n'  )
        if not opcion in opciones:
            print('Opcion Invalida. Intenta de nuevo')
        else:
            return opcion

def pedir():
    if 