# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 20:51:49 2022

@author: Renato
"""
A=[[2, 4, 5],[5, 6, 7],[4, 6, 7]]
#Imprime la columna i
print()
for fila in A:
    print("[ ",end="")
    for elemento in fila:
        print("{}".format(elemento),end=" ")
    print("]")
print()
i=2
columna = [fila[i] for fila in A]













print(A[2][0])

#Imprime Matriz
# for i in range(len(A)):
#         print("[ ",end="")
#         for j in range(len(A[i])):
#             print(A[i][j],end=" ")
#         print("]")

#Imprime la columna i
# i=2
# columna = [fila[i] for fila in A]
# print(columna)

# Imprime la fila i
# i=1
# fila =(A[i])
# print(fila)


#Suma todos los elementos de la matriz
# acu=0
# for i in range(len(A)):
#         for j in range(len(A[i])):
#             acu=acu+A[i][j]
# print(acu)

#Suma todas las filas de una matriz
# suma_filas=[]
# for f in A:
#     suma_filas.append(sum(f))
# print(suma_filas)


#Suma todas las columnas de una matriz DEBER

  




