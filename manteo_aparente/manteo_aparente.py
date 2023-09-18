import tkinter as tk
from tkinter import messagebox
from tkinter import *
import numpy as np
import os

# Definir rutas relativas
ruta = os.path.abspath(__file__)
direct = os.path.dirname(ruta)

# Unir rutas
rutaico = os.path.join(direct, "resources/compas.ico")
rutaref = os.path.join(direct, "resources/figura1.png")
def calcular():
    # Extraer información de los entry
    entrada = entry.get()
    entrada1 = entry1.get()
    
    # Verificar si es un número válido
    try:
        mreal = float(entrada)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido (0-90)")
        return
    
    try:
        alpha = float(entrada1)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido (0-90)")
        return

    # Calculos de numpy

    # Convertir de grados a radianes
    mrealrad = np.deg2rad(mreal)
    alpharad = np.deg2rad(alpha)

    # Calcular el producto de manteo real por ángulo alpha
    prodrad = np.multiply(np.tan(mrealrad),np.sin(alpharad))

    # Calcular arcotangente de prodrad
    maparenterad = np.arctan(prodrad)

    # Convertir rad a dg
    maparentedg = np.multiply(maparenterad , np.divide(180 , np.pi))

    # Redondear
    resultado = np.round(maparentedg,decimals=2)

    
    # Mostrar el resultado
    messagebox.showinfo("Resultado", f"El manteo aparente es: {resultado} grados")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Calculadora manteo aparente - P. Martínez")
ventana.iconbitmap(rutaico)
ventana.config(bg="white")

# Importar imagen
fig1 = PhotoImage(file=rutaref)

# Plotear imagen
label = Label(text="β es el manteo real y α el ángulo del plano respecto al rumbo en el que se mide el plano")
label.config(image=fig1)
label.config(compound=LEFT)
label.config(bg="white")
label.grid(row=0,column=0)

# Frames de orden
fr1 = Frame(ventana)
fr1.grid(row=1,column=0)
fr1.config(bg="white")

fr2 = Frame(fr1)
fr2.grid(row=0,column=0)
fr2.config(width=50,height=60)
fr2.config(bg="white")

fr3 = Frame(fr1)
fr3.grid(row=2,column=0)
fr3.config(width=50,height=60)
fr3.config(bg="white")

fr4 = Frame(ventana)
fr4.config(bg="white")
fr4.grid(row=4,column=0)
fr4.config(height=50)

# Labels de instrucciones
lbl = Label(fr1, text="Manteo real (0°-90°)")
lbl.config(bg="white")
lbl.grid(row=1,column=0)

lbl1 = Label(fr1, text="Ángulo α (0°-90°)")
lbl1.config(bg="white")
lbl1.grid(row=1,column=2)

# Crear entry para manteo real
entry = tk.Entry(fr1)
entry.grid(row=1,column=1)
entry.config(bg="lightgray")


# Crear entry para alpha
entry1 = tk.Entry(fr1)
entry1.grid(row=1,column=3)
entry1.config(bg="lightgray")

# Crear un botón para realizar el cálculo
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.grid(row=2,column=0)
boton_calcular.config(width=20,height=2)

# Ejecutar la interfaz gráfica
ventana.mainloop()