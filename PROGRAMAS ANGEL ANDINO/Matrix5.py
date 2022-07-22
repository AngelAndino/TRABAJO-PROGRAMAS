# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 20:42:22 2022

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
def Imprime(A):
    for fila in A:
        print("[ ",end="")
        for elemento in fila:
            print("{}".format(elemento),end=" ")
        print("]")
    print()

print('MATRIZ A')
Imprime(A)
print('MATRIZ B')
Imprime(B)
print('MATRIZ C')
Imprime(C)