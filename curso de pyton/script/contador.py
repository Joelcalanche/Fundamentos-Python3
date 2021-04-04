# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 07:26:18 2021

@author: calanche
"""
from io import open
import sys
fichero = open("contador.txt","a+")
fichero.seek(0)
contenido = fichero.readline()
if len(contenido)==0:
    contenido = "0"
    fichero.write(contenido)
fichero.close()


# Vamos a intentar transformar el texto a un numero
try:
    contador = int(contenido)
    
    # En funcion de lo que el usuario quiera..
    # el minimo numero de argumentos sera 2, el primero es el nombre del script
    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            contador += 1
        elif sys.argv[1] =="dec":
            contador -= 1
    print(contador) 
    
    # Finalmente volvemos a escribir los cambios en el fichero
    fichero = open("contador.txt","w")
    fichero.write(str(contador))
    fichero.close()
except:
    print("error: Fichero corrupto.")
        
            
        
