# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from io import open

fichero = open("personas.txt","r",encoding="utf8")
lineas = fichero.readlines()
fichero.close()
del(fichero)
personas = []
for linea in lineas:
    
    campos = linea.replace("\n", "").split(";")
    persona = {
               "id":campos[0],
               "nombre":campos[1],
               "apellido":campos[2],
               "nacimiento":campos[3]
                }
    personas.append(persona)
#print(personas)
for p in personas:
    print(f"(id= {p['id']}), {p['nombre']} {p['apellido']} => {p['nacimiento']}")
    
    
    