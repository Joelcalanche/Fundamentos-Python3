# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 10:52:18 2021

@author: User
"""


from setuptools import setup

setup(
      name ="paquete",
      version = "0.1",
      description = "Este es un paquete de ejemplo",
      author = " joel calanche",
      author_email = "joelcalanche96@♠gmail.com",
      script = [],
      # lo mas importante incluir los paquetes y los subpaquetes
      packages =["paquete","paquete.adios", "paquete.hola"]
      
      )


