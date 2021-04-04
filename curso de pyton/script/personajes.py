# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 08:03:53 2021

@author: calanche
"""

from io import open
import pickle
class Personaje:
    def __init__(self, nombre, vida, ataque, defenza, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defenza = defenza
        self.alcance = alcance
        
    def __str__(self):
        
        return f"{self.nombre}=> {self.vida} vida, {self.ataque} ataque, {self.defenza} defenza, {self.alcance} alcance"
    
    

        
class Gestor:
    
    personajes = []
    
    # Constructor de clase
    def __init__(self):
        self.cargar()
       
    def agregar(self,p):
        for pTemp in self.personajes:
            
            if pTemp.nombre == p.nombre:
                return
            
        self.personajes.append(p)
        self.guardar()
               
    def borrar(self, nombre):
        for pTemp in self.personajes:
            
            if pTemp.nombre == nombre:
                self.personajes.remove(pTemp)
                self.guardar()
                
                print(f"\nPersonaje{nombre} borrado")
                return
            

        
    def mostrar(self):
        if len(self.personajes) == 0:
            print("El gestor esta vacio")
            return
        for p in self.personajes:
            print(p)
    def cargar(self):
        # lo abriremos como append binario con funciones de lectura
        fichero = open("personajes.pckl", "ab+")
        fichero.seek(0)
        try:
            # la primera vez que abramos el fichero estara vacio, nos dara error
            self.personajes = pickle.load(fichero)
        except:
            #print("El fichero esta vacio")
            pass
        finally:
            # super importante cerrar el fichero
            fichero.close()
            del(fichero)
            print(f"Se han cargado {len(self.personajes)} personajes")
            
    def guardar(self):
        fichero = open("personajes.pckl","wb")
        pickle.dump(self.personajes, fichero)
        fichero.close()
        del(fichero)
        
        

G = Gestor()
#G.mostrar()
#G.agregar(Personaje("Caballero", 4, 2, 4, 2))
#G.agregar(Personaje("Guerrero", 2, 4, 2, 4))
#G.agregar(Personaje("Arquero", 2, 4, 1, 8))
#G.mostrar()
G.borrar("Arquero")
G.mostrar()

    