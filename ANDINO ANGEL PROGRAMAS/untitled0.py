#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 21:24:01 2022

@author: veronicarodriguez
"""

contador=0
contador_igual=0
contador_negativo=0
while True:
    while True:
        contador+=1
        num1=int(input("Ingrese el primer número: "))
        num2=int(input("Ingrese el segundo número: "))
        if num1==num2 :
            print("Error, los dos números no deben ser iguales")
        elif num1<0 or num2<0:
            print("Error, los dos números no deben ser negativos")
            contador_negativo+=1
        else:
            break
    print("Las veces que se ha ejecutado el programa es:",contador)
    print("Las veces que se digitaron números iguales es:",contador_igual)
    print("Las veces que se digitaron números negativos es:",contador_negativo())
    print("El promedio de las veces que se ejecuto el programa con números negativos:",contador_negativo/contador)
    print("El promedio de las veces que se ejecuto el programa con números iguales:",contador_igual/contador)
    salir=input("Para salir, digite si, caso contrario digite cualquier tecla: ")
    if salir== "si" or salir== "SI" or salir=="Si" or salir=="sI":
        break
    