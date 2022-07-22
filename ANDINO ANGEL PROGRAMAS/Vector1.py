# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 11:27:42 2022

@author: Renato
"""

t=int(input('Ingrese el tamaño del vector:'))
a=[]
acu=0
for i in range(t):
    a.append([0])

for i in range(t):
    a[i]=int(input('Ingrese el elemento {}:'.format(i+1)))
    acu=acu+a[i]
print(a)
print('La suma es:',acu)