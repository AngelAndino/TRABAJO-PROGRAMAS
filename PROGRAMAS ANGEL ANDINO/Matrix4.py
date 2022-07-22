# -*- coding: utf-8 -*-
"""
Created on Sat May 28 20:45:45 2022
Tema: Suma de dos matrices
@author: Renato
"""
a=int(input('Ingrese el número de filas:'))
b=int(input('Ingrese el número de columnas:'))
A=[]
B=[]
C=[]
for i in range(a):
    A.append([])
    B.append([])
    C.append([])
for i in range(a):
    for j in range(b):
        valor1=int(input('Fila A{},Columna A{}:'.format(i+1, j+1)))
        valor2=int(input('Fila B{},Columna B{}:'.format(i+1, j+1)))
        valor3=valor1+valor2
        A[i].append(valor1)
        B[i].append(valor2)
        C[i].append(valor3)
print('MATRIZ A')
for fila in A:
    print("[ ",end="")
    for elemento in fila:
        print("{}".format(elemento),end=" ")
    print("]")
print()        

print('MATRIZ B')
for fila in B:
    print("[ ",end="")
    for elemento in fila:
        print("{}".format(elemento),end=" ")
    print("]")
print()  
      
print('MATRIZ C  --SUMA DE A y B--')
for fila in C:
    print("[ ",end="")
    for elemento in fila:
        print("{}".format(elemento),end=" ")
    print("]")
print()        
        