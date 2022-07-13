# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 11:48:28 2022

@author: Programación
"""

t=int(input("Ingrese el tamaño del vector: "))
a=[]
b=[]
for i in range(t):
    a.append([0])
    b.append([0])
for i in range(t):
    a[i]=int(input("Ingrese el elemento a[{}]:".format(i+1)))
for i in range(t):
    b[i]=int(input("Ingrese el elemento b[{}]:".format(i+1)))

print("a=",a)
print("b=",b)