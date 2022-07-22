# -*- coding: utf-8 -*-
"""
Creat+ed on Fri May 27 22:27:51 2022
Tema: Insertar un vector de tam ingresado desde teclado y suma elementos
@author: Renato

"""

a=int(input('Ingrese el tamaño del Vector:'))
vec=[]
sum=0
for i in range(a):
    vec.append([0])
for i in range(a):
    vec[i]=int(input('Elemento {}: '.format(i+1)))
    sum=sum+vec[i]
print('La suma es:',sum)
