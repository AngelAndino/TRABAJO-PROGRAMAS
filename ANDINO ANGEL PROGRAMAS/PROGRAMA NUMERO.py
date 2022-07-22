# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 12:23:06 2022

@author: Dell
"""

b=int(input('Ingrese un número: '))
a=int(input('Ingrese un número: '))
suma=0
for i in range (1,a+1):
    
    suma+=pow(b,2*i)
print("La suma es", suma)