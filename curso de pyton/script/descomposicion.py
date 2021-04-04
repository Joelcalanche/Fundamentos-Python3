# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 13:23:40 2021

@author: User
"""

import sys
# el primer argumento siempre es el nombre del fichero
if len(sys.argv) == 2:
    numero = int(sys.argv[1])
    if numero < 0 or numero > 9999:
        print("error numero incorrecto")
            
        print("ejemplo: descomposicion.py[0-9999]")
    else:
        # aqui va la logica
         # len solo funciona con listas y cadenas de caracteres
         cadena = str(numero)
         longitud = len(cadena)
         
         for i in range(longitud):
             # para recorrer al revez restamos al total-1 - i, el -1 es porque en python se empieza desde el 0
             print("{:04d}".format(int(cadena[longitud- 1 -i]) * 10 ** i))
else:
    print("error argumentos incorrectos")
    
    print("ejemplo: descomposicion.py[0-9999]")
    