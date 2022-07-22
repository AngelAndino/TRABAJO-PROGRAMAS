#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 21:45:13 2022

@author: veronicarodriguez
"""

numero=1
sumainter=0
contador1=0
suma1=0
contador2=0
while True:
    num1=int(input("Ingrese el primer número: "))
    num2=int(input("Ingrese el segundo número: "))
    if num1==num2:
        print("Error, los números son iguales")
    else:
        break
if num1>num2:
    minimo=num2
    maximo=num1
else:
    minimo=num1
    maximo=num2
while True:
    numero=int(input("Digite un número: "))
    if numero==0:
        break
    
    if numero>minimo and numero<maximo:
        sumainter+=numero
    elif numero<minimo or numero>maximo:
        suma1+=numero
        contador1+=1
    elif numero==minimo or numero==maximo:
        contador2+=1
print("La suma de los números que están dentro del intervalo son: ",sumainter)
print("El promedio de los números fuera del intervalo son: ",suma1/contador1)
print("La cantidad de números iguales a los límites del intervalo son: ",contador2)
print("Fin del programa")
