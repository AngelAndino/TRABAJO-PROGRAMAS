# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 20:15:06 2022

@author: S7
"""

numero=1
sumainterna=0
contador1=0
suma1=0
contador2=0
while True:
    num1=int(input("Ingrese el primer numero: "))
    num2=int(input("Ingrese el segundo numero: "))
    if num1==num2:
        print("Error los numeros son iguales")
    else:
        break
if num1>num2:
    minimo=num1
    maximo=num2
else:
    minimo=num1
    maximo=num2
while numero!=0:
    numero=int (input("Digite un numero: "))
    if numero>minimo and numero<maximo:
        sumainterna+=numero
    elif numero<minimo or numero>maximo:
        suma1+=numero
        contador1+=1
    elif numero==minimo or numero==maximo:
        contador2+=1
print("La suma de los numeros que estan dentro del intervalo es:",sumainterna)
print("El promedio de los numeros fuera del intervalo es:",suma1/contador1)
print("la cantidad de numeros iguales a los limites del intervalo es:",contador2)
print("Fin del programa :")
        