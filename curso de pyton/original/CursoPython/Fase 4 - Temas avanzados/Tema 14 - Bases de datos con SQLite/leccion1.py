# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 09:32:13 2021

@author: calanche
"""

# Conexion a la base de datos
import sqlite3
conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor()  

# Para crear una tabla
#cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100) )")
#cursor.execute("INSERT INTO usuarios(nombre, edad, email) VALUES ('Joel',25,'joel@ejemplo.com');")             
# tenemos algo asi como un sistema de  seguridad que nos pide confirmar los cambios  despues de haber ejecutado la orden
#conexion.commit()
# el cursor almacena los resultados de la consulta
#cursor.execute("""
#               SELECT * FROM usuarios
#               """)
#print(cursor)               
# recupere el primer registro en forma de tupla
# cada ves que se ejecuta fetchone se mueve el cursor a la posicion siguiente
#usuario = cursor.fetchone()
#print(usuario[2])
# para insertar varios elementos de un solo golpe
# definimos una lista de tuplas
#usuarios =[
#    ('Mario',51,'mario@ejemplo.com'),
#    ('Mercedes',38,'mario@ejemplo.com'),
#    ('Juan',19,'juan@ejemplo.com')
#    ]

# para ejecutar varias consultas usamos .executemany y una lista de tuplas
#cursor.executemany("""
#                   INSERT INTO usuarios VALUES(?,?,?)
                   
#                   """,usuarios)
## El commit() es como un guardar

# Recuperar de forma masiva varios registros

cursor.execute("SELECT * FROM usuarios")


# con .fetchall recuperamos todos los registros que me devuelve el cursor, luego de la consulta
usuarios = cursor.fetchall()

# Me lo devuelve en formato de lista de tuplas
print(usuarios)

for usuario in usuarios:
    print(f" nombre: {usuario[0]}",f"email: {usuario[1]}")

conexion.commit()              

conexion.close()
