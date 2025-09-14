from menu import MENU_ITEMS
empleados = []

# Inicializo el programa
def inicio():
    while True:
        nombre= input('Bienvenido a HamburguesasIT \n Por favor introduzca su nombre:')
        if nombre in empleados:
            print('Recuerde siempre recibir al cliente con una sonrisa :)')
            