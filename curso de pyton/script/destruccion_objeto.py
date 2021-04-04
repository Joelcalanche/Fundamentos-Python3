# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 10:06:13 2021

@author: User
"""

class Pelicula:
    # constructo clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print(" se ha creado una pelicula ", self.titulo)
        # existe un metodo destructor que se ejecuta  cuando decidimos borrar una instancia
    # destructor de clase
    def __del__(self):
        print(" se esta borrando la pelicula",self.titulo)
p = Pelicula("El padrino", 175,1972)
del(p)