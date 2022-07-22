# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 09:09:44 2022

@author: Renato
"""

A=[[2, 4, 5],[5, 6, 7],[4, 6, 7],[1, 0, 1]]
filas=len(A)
columnas=len(A[0])
print(A[2][2])
print('Filas:',filas)
print('Columnas:',columnas)

print()
for fila in A:
    print("[ ",end="")
    for elemento in fila:
        print("{}".format(elemento),end=" ")
    print("]")
print()        
    