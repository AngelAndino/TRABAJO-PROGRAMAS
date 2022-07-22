# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 11:30:26 2022

@author: Renato
"""

A=[[2, 4, 5],[5, 6, 7],[4, 6, 7],[4, 6, 7]]
B=[[2, 4, 5],[5, 6, 7]]
C=[[2, 4, 5],[5, 6, 7],[4,1,5]]

def Imprime(A):
    print()
    for fila in A:
        print("[ ",end="")
        for elemento in fila:
            print("{}".format(elemento),end=" ")
        print("]")
    print()        
Imprime(A)
Imprime(B)
Imprime(C)






