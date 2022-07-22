# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 12:36:00 2022

@author: Renato
"""
a=int(input('Ingrese el valor:'))
acu=0
cont=1
for i in range(1,a+1):
    acu=acu+cont
    cont=cont+2
print(acu)