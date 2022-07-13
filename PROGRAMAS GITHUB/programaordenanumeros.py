# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 21:36:06 2022

@author: Programación
"""

num1=int(input('Ingrese primer número: '))
num2=int(input('Ingrese segundo  número: '))
num3=int(input('Ingrese tercer número: '))
if num1>num2:
    if num2>num3:
        print(num1,' ',num2,' ',num3)
elif num2>num3:
    print(num2,' ',num1,' ',num3)
else:
    print(num3,' ',num2,' ',num1)
