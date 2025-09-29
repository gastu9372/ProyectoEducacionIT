import tkinter as tk
from tkinter import simpledialog
from pedido import Pedido
from encargados import Encargado, EMPLEADOS
from bbddmanager import DBManager

db = DBManager()
encargado_actual = None
pedido_actual = None

# --- Funciones ---
def login_encargado():
    global encargado_actual
    nombre = simpledialog.askstring("Login", "Ingrese su nombre de encargado:")
    if not nombre:
        return
    empleado = next((e for e in EMPLEADOS if e.nombre.lower() == nombre.lower()), None)
    if empleado:
        encargado_actual = Encargado(empleado)
        encargado_actual.login(db)
        lbl_encargado.config(text=f"Encargado: {empleado.nombre}")
    else:
        lbl_status.config(text="⚠️ Encargado no encontrado")
        
def logout_encargado():
    global encargado_actual
    if encargado_actual:
        encargado_actual.logout(db)   # guarda OUT en la DB con caja
        lbl_status.config(text=f"👋 Encargado {encargado_actual.empleado.nombre} cerró turno")
        encargado_actual = None
        lbl_encargado.config(text="Encargado: no logueado")
    else:
        lbl_status.config(text="⚠️ No hay encargado activo")


def nuevo_pedido():
    global pedido_actual
    if not encargado_actual:
        lbl_status.config(text="⚠️ Primero loguee un encargado")
        return
    cliente = entry_cliente.get().strip()
    if not cliente:
        lbl_status.config(text="⚠️ Ingrese nombre del cliente")
        return
    pedido_actual = Pedido(cliente, encargado_actual.empleado.nombre)
    lbl_status.config(text=f"Nuevo pedido para {cliente}")
    actualizar_resumen()

def agregar_item(codigo):
    if not pedido_actual:
        lbl_status.config(text="⚠️ Cree un pedido primero")
        return
    pedido_actual.agregar_item(codigo, 1)
    actualizar_resumen()

def actualizar_resumen():
    if pedido_actual:
        resumen = " | ".join(f"{c}: {pedido_actual.items.get(c,0)}" for c in ["S","D","T","F"])
        lbl_resumen.config(text=f"Pedido: {resumen} - Total USD ${pedido_actual.total}")

def hacer_pedido():
    if not pedido_actual:
        lbl_status.config(text="⚠️ No hay pedido para guardar")
        return
    pedido_actual.guardar_en_db(db)
    lbl_status.config(text="✅ Pedido guardado")
    entry_cliente.delete(0, tk.END)
    lbl_resumen.config(text="")
    
def cancelar_pedido():
    global pedido_actual
    pedido_actual = None
    entry_cliente.delete(0, tk.END)
    lbl_resumen.config(text="")
    lbl_status.config(text="Pedido cancelado")

def salir_seguro():
    if encargado_actual:
        encargado_actual.logout(db)
    root.destroy()

# --- GUI ---
root = tk.Tk()
root.title("Sistema de Ventas")
root.geometry("400x400")

lbl_encargado = tk.Label(root, text="Encargado: no logueado")
lbl_encargado.pack()

btn_login = tk.Button(root, text="Iniciar turno Encargado", command=login_encargado)
btn_login.pack(pady=5)

btn_logout = tk.Button(root, text='Finalizar turno', command=logout_encargado)
btn_logout.pack(pady=5)

tk.Label(root, text="Cliente:").pack()
entry_cliente = tk.Entry(root)
entry_cliente.pack()

btn_nuevo = tk.Button(root, text="Nuevo Pedido", command=nuevo_pedido)
btn_nuevo.pack(pady=5)

frame_items = tk.Frame(root)
frame_items.pack(pady=5)

tk.Button(frame_items, text="Combo S", command=lambda: agregar_item("S")).grid(row=0, column=0)
tk.Button(frame_items, text="Combo D", command=lambda: agregar_item("D")).grid(row=0, column=1)
tk.Button(frame_items, text="Combo T", command=lambda: agregar_item("T")).grid(row=0, column=2)
tk.Button(frame_items, text="Flurby",  command=lambda: agregar_item("F")).grid(row=0, column=3)

lbl_resumen = tk.Label(root, text="")
lbl_resumen.pack(pady=5)

btn_pedido = tk.Button(root, text="Hacer Pedido", command=hacer_pedido)
btn_pedido.pack(pady=5)

btn_cancelar = tk.Button(root, text="Cancelar Pedido", command=cancelar_pedido)
btn_cancelar.pack(pady=5)

btn_salir = tk.Button(root, text="Salir Seguro", command=salir_seguro)
btn_salir.pack(pady=5)

lbl_status = tk.Label(root, text="")
lbl_status.pack()

root.mainloop()
