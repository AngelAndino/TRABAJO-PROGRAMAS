# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 00:00:16 2022

@author: Renato
"""
import funcion as f1
b=int(input('Ingrese la base:'))
h=int(input('Ingrese la altura:'))
Respuesta=f1.AreaT(b, h)
print('EL área del triángulo es:', Respuesta)
l1=int(input('Ingrese el un lado:'))
l2=int(input('Ingrese el otro lado:'))
Respuesta2=f1.AreaR(l1, l2)
print('EL área del rectángulo es:', Respuesta2)
