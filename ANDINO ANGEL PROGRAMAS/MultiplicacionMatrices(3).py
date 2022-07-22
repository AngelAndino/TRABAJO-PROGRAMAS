# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 10:13:38 2022

@author: Renato
"""

a = [
    [3, 2, 1],
    [1, 1, 3],
    [0, 2, 1],
]
b = [
    [2, 1],
    [1, 0],
    [3, 2],
]
filas_a = len(a)
filas_b = len(b)
columnas_a = len(a[0])
columnas_b = len(b[0])

# Asignar espacio al producto. Es decir, rellenar con "espacios vacíos"
producto = []
for i in range(filas_b):
    producto.append([])
    for j in range(columnas_b):
        producto[i].append(None)
        
# Rellenar el producto
for c in range(columnas_b):
    for i in range(filas_a):
        suma = 0
        for j in range(columnas_a):
            suma += a[i][j]*b[j][c]
        producto[i][c] = suma

def Imprimir(A):
    print()
    for i in A:
        print("[ ",end="")
        for j in i:
            print("{}".format(j),end=" ")
        print("]")
    print()

Imprimir(a)
Imprimir(b)
Imprimir(producto)