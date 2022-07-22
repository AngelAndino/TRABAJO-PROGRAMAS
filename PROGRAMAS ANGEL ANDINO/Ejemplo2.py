# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 00:26:43 2022

@author: Renato
"""
import math
n=int(input('Ingrese un Número:'))
while n>10:
    n=math.trunc(n/10)
print('El primer dígito es:',n)