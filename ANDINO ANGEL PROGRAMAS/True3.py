# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:33:37 2022

@author: Renato
"""

a=int(input('Ingrese Intervalo Inferior:'))
b=int(input('Ingrese Intervalo Superior:'))
i=1
while a==b or a>b:
    print('Inserte Nuevamente los datos')
    a=int(input('Ingrese Intervalo Inferior:'))
    b=int(input('Ingrese Intervalo Superior:'))
    i=i+1

print('Ah ingresado {} veces incorrectas'.format(i))
    