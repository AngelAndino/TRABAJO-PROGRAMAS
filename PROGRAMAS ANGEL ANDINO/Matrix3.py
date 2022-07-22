# -*- coding: utf-8 -*-
"""
Created on Fri May 27 23:45:21 2022

@author: Renato
"""

a=int(input('Ingrese el número de filas:'))
b=int(input('Ingrese el número de columnas:'))
A=[]
for i in range(a):
    A.append([])
    for j in range(b):
        valor=float(input('Fila {},Columna {}:'.format(i+1, j+1)))
        A[i].append(valor)

print()
for fila in A:
    print("[",end="")
    for elemento in fila:
        print("{:8.2f}".format(elemento),end="")
    print("]")
print()        
    