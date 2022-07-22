# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 13:19:08 2022

@author: lab
"""

#while
num=0 #Definir una variable igual a 0
while(num<2 or num>99): #Mientras num es menor a 2 o num es mayor a 99
    num = int(input("Ingrese hasta que numero desea imprimir: "))#Pedir ingresar por teclado un numero para imprimir las tablas
    if (num<2 or num>99):#Si num es menor a 2 o num es mayor a 99
        print("El numero debe ser mayor a 2 y menor a 100")#Imprimir el numero debe ser mayor a 2 y menor a 100

print("")#Imprimir espacio en blanco
j=1#Definir variable j igual a 1
while(j<num+1): #Mientras j es menor a num+1
    suma=0 #Variable suma es igual a 0
    contador3=0 #Definir contador3 es igual a 0
    contador5=0 #Definir contador5 es igual a 0
    contadorpar=0 #Definir contadorpar es igual a 0
    contadorimpar=0 #Definir contadorimpar es igual a 0
    print("Tabla del",j)#Imprimir Tabla del,j
    i=1#Definir variable i es igual a 1
    while (i<16): #Mientras i es menor a 16
        multiplicacion = j * i #Operación multiplicación variable j por i
        if (multiplicacion%5)==0: #Si la multiplicacion del mudulo de 5 es igual a 0
            contador5+=1 #Contador5 es igual a contador5 más uno
        if (multiplicacion%3)==0:##Si la multiplicacion del modulo de 3 es igual a 0
            contador3+=1 #Contador3 es igual a contador3 más uno
        if (multiplicacion%2)==0:#Si la multiplicacion del modulo de 2 es igual a 0
            contadorpar+=1#Contadorpar es igual a contadorpar más uno
        else: #Si no
            contadorimpar+=1 
        suma+=multiplicacion#Suma es igual a suma más multi#Contadorimpar es igual a contadorpar más uno multiplicación 
        print(j,"x" ,i ,"=", multiplicacion)#Imprimir la multiplicación
        i+=1#Variable i es igual a i más 1
    print("La suma de los numeros es: ",suma) #Imprimir la suma de los numero es, variable suma
    print("El promedio de los numeros es: ",suma/15)#Imprimir el promedio de los numero es, variable promedio
    print("Los multipolos de 3 son: ",contador3)#Imprimir el multiplo de 3 de los numero es, contador3
    print("Los multiplos de 5 son: ",contador5)#Imprimir el multiplo de 5 los numero es, contador5
    print("Los numeros pares son: ",contadorpar)#Imprimir los numeros pares son, contadorpar
    print("Los numeros impares son: ",contadorimpar)#Imprimir los numeros impares son, contadorimpar
    j+=1#Variable j es igual a j más 1