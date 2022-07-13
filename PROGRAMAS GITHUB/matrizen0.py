# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 11:38:25 2022

@author: Dell
"""

matriz=[]
filas=4
columna=4
for i in range(filas):
    matriz.append([0])
    for j in range(columna-1):
        matriz[i].append(0)

matriz[3][2]=90