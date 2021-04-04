# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 19:14:27 2021

@author: User
"""

def suma(a,b):
    try:
        r = a + b
        
    except TypeError:
        print("error: tipo de dato no valido")
        
    else:
        return r
            

def resta(a,b):
    try:
        r = a - b
        
    except TypeError:
        print("error: tipo de dato no valido")
        
    else:
        return r
            
    

def producto(a,b):
    try:
        r = a * b
        
    except TypeError:
        print("error: tipo de dato no valido")
        
    else:
        return r
            

def division(a,b):
    try:
        r = a / b
        
    except TypeError:
        print("error: tipo de dato no valido")
    except ZeroDivisionError:
        print("error: no es posible dividir por cero ")
        
        
    else:
        return r
            


