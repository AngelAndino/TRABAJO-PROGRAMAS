# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 14:13:58 2022

@author: lab
"""

def suma (*a):
    print("\n Tipo de datos del argumento:",type(a))
    suma=0
    for n in a:
        suma+=n
    print("suma:",suma)
suma(3,5,8,6)
        