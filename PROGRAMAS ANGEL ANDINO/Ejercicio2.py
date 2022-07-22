# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 10:06:32 2022

@author: Renato
"""
a=int(input("Ingrese el número:"))
t=int(input("Ingrese el Intervalo:"))

print("   |",end="")

for i in range(1,a+1):
    print(t*i, end=" ")
print()

for i in range(1,i*t):
    print('-', end="")