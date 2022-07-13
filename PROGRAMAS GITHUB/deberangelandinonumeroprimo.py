# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 23:22:07 2022

@author: Angel Andino
"""

num=int(input('Ingrese un numero:'))
def NumeroPrimo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo")
            return False
        if num%n!=0:
            print("Es primo")
            return True
print(NumeroPrimo(num))