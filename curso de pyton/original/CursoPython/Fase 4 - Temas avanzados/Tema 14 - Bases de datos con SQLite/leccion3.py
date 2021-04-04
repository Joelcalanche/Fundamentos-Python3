# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 13:04:06 2021

@author: calanche
"""
import sqlite3
conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

# Podemos realizar consultas especificas utilizando la clausula WHERE

# Esta consulta me devolvera las filas donde el id sea 1
#cursor.execute("SELECT * FROM usuarios WHERE edad='27'")
# fetch significa buscar o extraer
#usuarios = cursor.fetchall()

#print(usuarios)

#cursor.execute("""
#               UPDATE usuarios SET nombre = 'Hector Costa', edad=30 
#               WHERE nombre LIKE '%Hector%'
               
#               """)

cursor.execute("""
               DELETE FROM usuarios  
               WHERE nombre LIKE '%Hector%'
               
               """)              
conexion.commit()
conexion.close()
