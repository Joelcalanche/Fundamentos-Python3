# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:34:01 2021

@author: calanche
"""

import sqlite3
from tkinter import *

# Configuracion de la raiz

root= Tk()

root.title("Bar Don Costa - Menu")

root.resizable(0,0)
root.config(bd= 25, relief ="sunken")

Label(root, text = "   Bar Don Costa   ", fg="darkgreen", font=("Times New Roman", 28, "bold italic")).pack()
Label(root, text = "   Menu del dia   ", fg="green", font=("Times New Roman", 24, "bold italic")).pack()

# Separacion de titulos y categorias
Label(root, text="").pack()

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()
# Buscar las categorias y platos de la bd
        
categorias = cursor.execute("""
                                
                              SELECT * FROM categoria  
                                
                                """).fetchall()
for categoria in categorias:
    Label(root, text = categoria[1], fg="black", font=("Times New Roman", 20, "bold italic")).pack()
    
    platos =  cursor.execute(f"""
                                 
                               SELECT * FROM plato WHERE categoria_id ={categoria[0]}
                                 
                                 """).fetchall() 
        
    for plato in platos:
        Label(root, text = plato[1], fg="gray", font=("Verdana", 15, "italic")).pack()
    

    # separacion entre categorias
    Label(root, text="").pack()


conexion.close()

# Precio del menu
Label(root, text = "12 (IVA incl.)", fg="darkgreen", font=("Times New Roman", 20, "bold italic")).pack(side="right")


# Finalmente ejecutamos el bucle de aplicacion
root.mainloop()