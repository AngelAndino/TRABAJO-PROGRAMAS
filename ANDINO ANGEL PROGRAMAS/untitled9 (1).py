#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 22:11:59 2022

@author: veronicarodriguez
"""

suma=0
contador3=0
contador5=0

for i in range (1,16):
    contador3=0
    contador5=0
    print("La tabla del número",i,"es: ")
    print("\n")
    for j in range (1,16):
        resultado=j*i
        if resultado%3==0:
            contador3+=1
        elif resultado%5==0:
            contador5+=1
        suma+=resultado
        print(i,"x",j,"=",resultado)
    print("La suma de los números es: ",suma)
    print("El promedio de los números es: ",suma/15)
    print("Los multiplos de 3 son: ",contador3)
    print("Los multiplos de 5 son: ",contador5)
    print("\n")
    