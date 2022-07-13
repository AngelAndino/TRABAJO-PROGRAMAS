# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 12:12:19 2022

@author: Dell
"""

m2=[0]*4
for i in range(4):
    m2[i]=[0]*4

for h in range (4):
    for y in range (4):
     t=int(input("Ingrese un valor a la lista: "))
     m2[h][y]=t

for h in range (4):
    for y in range (4):
        print(m2[h][y],end=" ")
    print(" ")