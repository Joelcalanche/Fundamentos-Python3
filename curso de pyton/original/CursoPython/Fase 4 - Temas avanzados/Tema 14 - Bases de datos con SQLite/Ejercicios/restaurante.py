# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:11:22 2021

@author: calanche
"""

import sqlite3


def crear_bd():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    
    try:
        cursor.execute("""
                       
                    CREATE TABLE categoria(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(100) UNIQUE NOT NULL)
                       
                       
                       """)
    except sqlite3.OperationalError:
        print("La tabla de categorias ya existe.")
    else:
        print("la tabla de categorias se ha creado correctamente.")
        
    try:
        cursor.execute("""
                       
                    CREATE TABLE plato(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(100) UNIQUE NOT NULL, 
                    categoria_id INTEGER NOT NULL,
                    FOREIGN KEY(categoria_id) REFERENCES categoria(id))
                       
                       
                       
                       """)                   
    except sqlite3.OperationalError:
        print("la tabla de platos ya existe ")
    else:
        print("la tabla de platos se ha creado correctamente")
    
    conexion.close()
def agregar_categoria():
    categoria= input("Nombre de la nueva categoria\n>")
    
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    
    try:
        cursor.execute(f"""
                       
                       INSERT INTO categoria VALUES(null,'{categoria}')
                       
                     
                       """)
    except sqlite3.IntegrityError:
        
        print(f"la categoria '{categoria}' ya existe")
    else:
        print(f"Categoria '{categoria}' creada correctamente")
                   
    conexion.commit()
    conexion.close()
    
def agregar_plato():
        
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    
    categorias = cursor.execute("""
                                
                              SELECT * FROM categoria  
                                
                                """).fetchall()
                                
    print("Selecciona una categoria para a;adir el plato:")
    for categoria in categorias:
        print(f"[{categoria[0]}] {categoria[1]}")
        
    categoria_usuario = int(input("> "))
    plato = input("Nombre del nuevo plato\n>")
    
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    
    try:
        cursor.execute(f"""
                       
                       INSERT INTO plato VALUES(null,'{plato}','{categoria_usuario}')
                       
                     
                       """)
    except sqlite3.IntegrityError:
        
        print(f"El plato ya existe '{plato}' ya existe")
    else:
        print(f"plato '{plato}' creado correctamente")
    
    
    
    
    conexion.commit()
    conexion.close()
    
        
def mostrar_menu():
    
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    
        
    categorias = cursor.execute("""
                                
                              SELECT * FROM categoria  
                                
                                """).fetchall()
    for categoria in categorias:
        print(categoria[1]) 
        platos =  cursor.execute(f"""
                                 
                               SELECT * FROM plato WHERE categoria_id ={categoria[0]}
                                 
                                 """).fetchall() 
        
        for plato in platos:
            print(f"\t{plato[1]}")                   
    
    
    
    
    conexion.close()
      
# Crear la base de datos
crear_bd()

# Menu de opciones del programa

while True:
    print("\nBienvenido al gestor del restaurante")
    opcion = input("/nIntruduce una opcion:\n[1] Agregar una categoria\n[2] Agregar un plato\n[3] Mostrar el menu\n[4]Salir del programa\n\n> ")
    
    if opcion == "1":
        agregar_categoria()
            
    elif opcion == "2":
        agregar_plato()
        
            
        
    elif opcion == "3":
       mostrar_menu()
        
        
    
            
    elif opcion == "4":
        print("Nos vemos!")
        
        break
    else:
        print("Opcion incorrecta")

        

    