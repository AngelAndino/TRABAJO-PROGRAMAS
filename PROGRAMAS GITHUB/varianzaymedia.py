# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 13:09:12 2022

@author: Dell
"""

def Media(vec, t):
    acu=0
    for i in range(t):
        acu+=vec[i]
    return acu/t

def Varianza(vec,t):
    acu=0
    for i in range(t):
        acu=acu+((vec[i]-Media(vec, t))**2)
    return acu/t

import math
t=int(input('Ingrese el tamaño del vector: '))
a=[0]*t
for i in range(t):
    a[i]=int(input('Ingrese el elemento a[{}]:'.format(i+1)))
print('a=',a)
print('La media es: ',Media(a, t))
print('La varianza es: ', Varianza(a, t))
print('La Desviasión media es: ', math.sqrt(Varianza(a, t)))