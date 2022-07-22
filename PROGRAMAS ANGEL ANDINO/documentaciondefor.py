# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 13:18:37 2022

@author: lab
"""

#for
num=0 #Definir una variable llamada num igual a cero 
while(num<2 or num>99):#Condicional Mientras num es menor a 2 o num es mayor a 99
    num = int(input("Ingrese hasta que numero desea imprimir la tabla de multiplicar:"))#Solicitar ingresar por teclado un numero para saber hasta que tabla imprimir
    if (num<2 or num>99):#Establecer una conidción Si num es menor a 2 o num es mayor a 99
        print("El numero debe ser mayor a 2 y menor a 100")#Imprimir en pantalla el numero debe ser mayor a 2 y menor a 100
print("") #Imprimir en pantalla un espacio en blanco
for j in range(1, num+1): #para variable j establecir  el rango de 1 a num más 1
    suma=0 #Se define una varibale suma igualada a cero 
    contador3=0 #Definir un contador3 igual a 0, para saber los múltiplos de 3  
    contador5=0 #Definir contador5 igual a 0, para saber los múltiplos de 5
    contadorpar=0 #Definir contadorpar igual a 0, para saber la cantidad de números pares
    contadorimpar=0 #Definir contadorimpar es igual a 0, para saber la cantidad de números impares
    print("Tabla del",j)#Imprimir Tabla del,variable j
    for i in range(1, 16): # para variable j establecer el rango de 1 a 16 para que se imprima la multiplicación de 1 a 15 
        multiplicacion = j * i #Establecer operacion de la multiplicacion de j por i 
        if (multiplicacion%5)==0: #Condición Si la multiplicacion del mudulo de 5 es igual a 0
           contador5+=1 #Contador5 es igual a contador5 más uno
        if (multiplicacion%3)==0:##Condición Si la multiplicacion del modulo de 3 es igual a 0
           contador3+=1 #Contador3 es igual a contador3 más uno
        if (multiplicacion%2)==0:#Condición Si la multiplicacion del modulo de 2 es igual a 0
           contadorpar+=1#Contador par es igual a contador par más uno
        else: #Caso contrario 
            contadorimpar+=1 #Contador impar es igual a contador impar más uno
        suma+=multiplicacion #Operación Suma es igual a suma más multiplicación
        print(j,"x" ,i ,"=", multiplicacion)#Imprimir la multiplicación variable j por i es igual a, multiplicación
    print("La suma de los numeros es: ",suma) #Imprimir por pantalla  la suma de los numero es, variable suma
    print("El promedio de los numeros es: ",suma/15)#Imprimir por pantalla el promedio de los numero es, variable suma divido para 15 
    print("Los multipolos de 3 son: ",contador3)#Imprimir por pantalla  el multiplo de 3 de los números es, contador3
    print("Los multiplos de 5 son: ",contador5)#Imprimir por pantalla  el multiplo de 5 de los números es, contador5
    print("Los numeros pares son: ",contadorpar)#Imprimir por pantalla los números pares son, contador par
    print("Los numeros impares son: ",contadorimpar)#Imprimir por pantalla  los numeros impares son, contador impar