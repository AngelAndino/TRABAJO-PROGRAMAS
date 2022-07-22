# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:07:56 2022

@author: Renato
"""
fil=int(input("Ingrese el número de filas: "))
col=int(input("Ingrese el número de columnas: "))
listaFilas=[]
listaColumnas=[]

for i in range(fil):
    listaFilas.append([])
    ele=int(input(f"Ingrese el elemento fila({i+1}):"))
    listaFilas[i].append(ele)   
for i in range(col):
    listaColumnas.append([])
    ele=int(input(f"Ingrese el elemento columna({i+1}):"))
    listaColumnas[i].append(ele) 

print(listaFilas)
print(listaColumnas)