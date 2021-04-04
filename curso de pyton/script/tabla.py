# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 13:03:06 2021

@author: User
"""

import sys
# el primer argumento siempre es el nombre del fichero
if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])
    if filas < 1 or filas > 9 or columnas < 1 or columnas > 9:
        print("error filas o columnas incorrectas")
            
        print("ejemplo: tabla.py[1-9[1-9]")
    else:
        # aqui empieza la logica
        for f in range(filas):
            # con este print vacio creamos una linea de separacion
            print("")
            for c in range(columnas):
                print(" * ", end= '')
                
        
else: 
    print("error argumentos incorrectos")
    
    print("ejemplo: tabla.py[1-9[1-9]")
    