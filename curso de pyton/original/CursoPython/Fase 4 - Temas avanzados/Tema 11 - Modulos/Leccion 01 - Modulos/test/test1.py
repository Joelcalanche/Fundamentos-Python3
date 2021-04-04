# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 09:13:31 2021

@author: User
"""

#mport saludos

#saludos.saludar()

# otra forma para importar solo la funcion que nos interesa
#from saludos import saludar

#saludar()

# si quieres importarlas todas de golpe
#from saludos import *

#saludar()
# con lo de arriba importamos todas las funciones


#from saludos import Saludo

#Saludo()

# consul
import sys
# con esto hacemos referencia al directorio anterior
sys.path.insert(1,'..')
print(sys.path)

from saludos import Saludo

Saludo()