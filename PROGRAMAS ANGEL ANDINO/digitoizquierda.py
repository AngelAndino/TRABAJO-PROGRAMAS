# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 11:27:10 2022

@author: Dell
"""
import math
def DígitoIzquierda(n):
    while n>10:
        n=math.trunc(n/10)
    return n

x=int(input('Digite un número: '))
print('El primer dígito es: ',DígitoIzquierda(x))

