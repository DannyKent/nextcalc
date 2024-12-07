import tkinter as tk
from tkinter import ttk, messagebox

# Funciones de la calculadora
def presionar_boton(valor):
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, actual + str(valor))

def calcular():
    try:
        expresion = entrada.get()
        resultado = eval(expresion)
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

def limpiar():
    entrada.delete(0, tk.END)

def sobre_nextcalc():
    messagebox.showinfo("Sobre NextCalc", "Infinia Computers INC \nDesarrollado por Danny Villarreal (Najash Code).\nNextCalc Versión 1.0\nTodos los derechos reservados 2024")

def sobre_infinia():
    messagebox.showinfo("Sobre Infinia", "Infinia Computers INC \nAlcalá de Guadaira Sevilla\nTeléfono 647915775\nMarca Registrada 2024")

def salir():
    ventana.quit()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("NextCalc")  
ventana.geometry("370x500")  
ventana.resizable(False, False)
ventana.attributes("-alpha", 0.96)
ventana.config(bg="#2B2B37")  

# Función para centrar la ventana en la pantalla
def centrar_ventana(ventana, ancho_ventana, alto_ventana):
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    pos_y = (alto_pantalla // 2) - (alto_ventana // 2)
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

centrar_ventana(ventana, 370, 500)

# Crear un menú
menu_bar = tk.Menu(ventana)
archivo_menu = tk.Menu(menu_bar, tearoff=0)
archivo_menu.add_command(label="Calculadora Científica")
archivo_menu.add_command(label="Convertidor")
archivo_menu.add_separator()
archivo_menu.add_command(label="Sobre NextCalc", command=sobre_nextcalc)
archivo_menu.add_command(label="Sobre Infinia", command=sobre_infinia)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=salir)

menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
ventana.config(menu=menu_bar)

# Entrada de texto
entrada = tk.Entry(
    ventana, font=("San Francisco", 28), justify="right",
    bd=0, bg="#3C3C49", fg="#FFFFFF"
)
entrada.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=(20, 10), padx=10, sticky="nsew")

# Configuración de colores
color_numeros = "#4D4D5A"  
color_operaciones = "#57ACFF"  
color_funciones = "#5C5C6D"  
color_texto = "#FFFFFF"  

# Botones de la calculadora
botones = [
    ("AC", 1, 0), ("±", 1, 1), ("%", 1, 2), ("/", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0, 2), (".", 5, 2), ("=", 5, 3),
]

# Estilos de botones
estilo_numeros = {"font": ("San Francisco", 20), "bg": color_numeros, "fg": color_texto, "bd": 1, "relief": "flat", "highlightthickness": 0}
estilo_operaciones = {"font": ("San Francisco", 20), "bg": color_operaciones, "fg": color_texto, "bd": 1, "relief": "flat", "highlightthickness": 0}
estilo_funciones = {"font": ("San Francisco", 20), "bg": color_funciones, "fg": color_texto, "bd": 1, "relief": "flat", "highlightthickness": 0}

# Crear y ubicar botones
for btn in botones:
    texto = btn[0]
    fila = btn[1]
    columna = btn[2]
    colspan = btn[3] if len(btn) == 4 else 1
    estilo = (
        estilo_operaciones if texto in "/+-*=." else
        estilo_funciones if texto in "AC±%" else
        estilo_numeros
    )
    boton = tk.Button(
        ventana, text=texto, 
        command=lambda t=texto: presionar_boton(t) if t not in "AC=" else limpiar() if t == "AC" else calcular(), 
        **estilo,
    )
    boton.grid(row=fila, column=columna, columnspan=colspan, sticky="nsew", padx=2, pady=2)

# Configuración de filas y columnas
for i in range(6):  
    ventana.grid_rowconfigure(i, weight=1)
for i in range(4):  
    ventana.grid_columnconfigure(i, weight=1)

# Iniciar bucle principal
ventana.mainloop()
