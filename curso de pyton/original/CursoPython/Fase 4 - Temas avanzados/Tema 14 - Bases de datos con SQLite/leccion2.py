# -*- coding: utf-8 -*-
"""
Trabajaremos las claves primarias, los campos incrementales y las claves unicas
"""
import sqlite3

# Creamos una base de datos
#conexion = sqlite3.connect("usuarios.db")
#cursor = conexion.cursor()
#cursor.execute("""
#               CREATE TABLE usuarios (
#                   dni VARCHAR(9) PRIMARY KEY,
#                   nombre VARCHAR(100),
#                   edad INTEGER,
#                   email VARCHAR(100) 
#                   )
               
#               """)
#usuarios =[
#    ('111111111A','Hector', 27, 'hector@ejemplo.com'),
#    ('222222222B','Mario', 51,'mario@ejemplo.com'),
#    ('333333333C','Mercedes',38,'mario@ejemplo.com'),
#    ('444444444D','Juan',19,'juan@ejemplo.com')
#    ]

#cursor.executemany("""
#                   
#                   INSERT INTO usuarios VALUES (?,?,?,?)
#                   
# 

#                  """,usuarios)             
#conexion = sqlite3.connect("productos.db")
#cursor = conexion.cursor()
#3cursor.execute("""
#               CREATE TABLE productos(
#                   id INTEGER PRIMARY KEY AUTOINCREMENT,
#                   nombre VARCHAR(100) NOT NULL,
#                   marca VARCHAR(100) NOT NULL,
#                   precio FLOAT NOT NULL
                   
                   
                   
#                   )
               
               
#               """)
#cursor = conexion.cursor()
#productos =[
#    ('Teclado','Logitech', 19.95),
#    ('Pantalla 19"','LG', 89.95)
#    ]
#cursor.executemany("""
#                   INSERT INTO productos VALUES(null,?,?,?)
                   
 #                  """,productos)

#cursor.execute("SELECT * FROM productos")

#productos = cursor.fetchall()

#for producto in productos:
#    print(producto)

# CLAVES UNICAS
conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

cursor.execute("""
               CREATE TABLE usuarios (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   dni VARCHAR(9) UNIQUE,
                   nombre VARCHAR(100),
                   edad INTEGER,
                   email VARCHAR(100)
                   
                   
                   )
               
               """)


usuarios =[
    ('111111111A','Hector', 27, 'hector@ejemplo.com'),
    ('222222222B','Mario', 51,'mario@ejemplo.com'),
    ('333333333C','Mercedes',38,'mario@ejemplo.com'),
    ('444444444D','Juan',19,'juan@ejemplo.com')
    ]               
cursor.executemany("""
                   
                   INSERT INTO usuarios VALUES (null,?,?,?,?)
                   
                   """, usuarios)
conexion.commit()
conexion.close()
