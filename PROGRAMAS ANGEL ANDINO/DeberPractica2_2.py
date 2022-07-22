# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:44:18 2022

@author: Renato
"""
a=int(input('Ingrese el número de filas:'))
b=int(input('Ingrese el número de columnas:'))
vec1=[]
vec2=[]
for i in range(a):
    vec1.append([0])
for i in range(a):
    vec1[i]=int(input('Elemento fila{}: '.format(i+1)))
    
for i in range(b):
    vec2.append([0])
for i in range(b):
    vec2[i]=int(input('Elemento columna{}: '.format(i+1)))

print(vec1)
print(vec2)