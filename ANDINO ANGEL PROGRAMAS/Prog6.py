# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 12:17:01 2022

@author: Renato
"""
a=int(input('Ingrese el valor:'))
acu=0
for i in range(1,a+1):
    print("1/",i**2, end="  ")
    acu=acu+(1/(i**2))
print()
print("La Suma es:",acu)
