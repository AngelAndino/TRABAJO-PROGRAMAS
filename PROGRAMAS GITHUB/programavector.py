# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 11:28:01 2022

@author: Programación
"""


vec=[]
t=int(input("Ingrese el tamaño del vector: "))
for i in range(t):
    vec.append([0])
for i in range(t):
    vec[i]=int(input('Ingrese el elemento {}: ' . format(i+1)))
print(vec)