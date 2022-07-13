# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 08:13:29 2022

@author: Angel Ismael Andino Noroña
"""

numfilas=[]
numcolumnas=[]

filas=int(input("Ingrese el numero de filas que desea en la matriz: "))
columnas=int(input("Ingrese el numero de columnas que desea en la matriz: "))

print("Inserte  los valores de las columnas a:")
for i in range(columnas):
    print("Ingrese a",i+1)
    numcolumnas.append(int(input()))

print("Inserte los valores de las las filas b:")
for i in range(filas):
    print("Ingrese b",i+1)
    numfilas.append(int(input()))

print("El resultado de la matriz formada es: ")
print("\t\t",end="")
for i in range(columnas):
    print(numcolumnas[i],end="  ")
print("")
for i in range(columnas*3):
    print("---",end="")
print("")
for i in range(filas):
    print(numfilas[i]," |",end="\t")
    for j in range(columnas):
        producto=numfilas[i]*numcolumnas[j]
        if producto>9:
            print(producto,end = " ")
        else:
            print(producto,end="  ")

    print("")