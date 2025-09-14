from menu import MENU_ITEMS
empleados = ['manuel']

# Inicializo el programa
def inicio():
    while True:
        nombre= input('Bienvenido a HamburguesasIT \n Por favor introduzca su nombre:')
        if nombre in empleados:
            print(nombre)
            print('Recuerde siempre recibir al cliente con una sonrisa :)')

#inicio()
            