# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 23:23:08 2022

@author: Renato
"""

A=[[2, 4, 5],[5, 6, 7],[4, 6, 7],[1, 0, 3],[3, 6, 1]]
#A=[[2,6,7,9,4,6,3],[3,6,2,5,8,2,5]]
# Imprimir la Matriz
def Imprimir(A):
    print()
    for i in A:
        print("[ ",end="")
        for j in i:
            print("{}".format(j),end=" ")
        print("]")
    print()    
Imprimir(A)


#Matriz Transpuesta
# B=[]
# for i in range(len(A[0])):
#     B.append([])
#     for j in range(len(A)):
#       B[i].append(A[j][i])  
# Imprimir(B)

#Linealizar por filas
# C=[]
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         C.append(A[i][j])  
# print(C)


#Linealizar por filas otra forma
# posicion=0
# D=[]
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         D.append([0])
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         D[posicion]=A[i][j]
#         posicion=posicion+1
# print(D)


#Linealizar por Columnas 
# pos=0
# dim=len(A)*len(A[0])
# E=[]
# for i in range(dim):
#         E.append([0])
# for i in range(len(A[0])):
#     for j in range(len(A)):
#         E[pos]=A[j][i]
#         pos=pos+1
# print(E)

#Linealizar por filas
# F=[]
# for i in range(len(A[0])):
#     for j in range(len(A)):
#         F.append(A[j][i])  
# print(F)




