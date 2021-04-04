# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 19:35:17 2021

@author: User
"""

import random
import math

def leer_numero(ini, fin, mensaje):
    while True:
        try:
            valor = int(input(mensaje))
        except:
            print("error: numero no valido")
        else:
            
            if valor >= ini and valor <= fin:
                break
            
        
    return valor



def generador():
    numeros = leer_numero(1,20,"¿Cuantos números quieres generar? [1-20]:")
    modo = leer_numero(1,3," Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: *.")

    lista = []
    
    for i in  range(numeros):
        numero = random.uniform(0, 101)
        if modo == 1:
            print(f"{numero} =>{math.ceil(numero)}")
            numero = math.ceil(numero)
        elif modo == 2:
            print(f"{numero} =>{math.floor(numero)}")
            numero = math.floor(numero)
        elif modo == 3:
            print(f"{numero} =>{round(numero)}")
            numero = round(numero)
            
        lista.append(numero)
    return lista



generador()
        
        
            
            