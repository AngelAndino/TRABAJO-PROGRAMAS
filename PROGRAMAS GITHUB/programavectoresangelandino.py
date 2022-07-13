# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 11:53:28 2022

@author: Angel Andino
"""

import numpy
while True:
    z=int(input('Digite el tamaño del vector:'))
    if z<5:
        print('Error el tamaño del vector tiene que ser mayor a 5')
    if z>30:
        print('Error el tamaño del vector tiene que ser mayor a 30')
    else:
        break
vector1=[0]*z
vector2=[0]*z
vector3=[0]*z

while True:
        vector1=numpy.random.randint(1,200,z).tolist()
        print(vector1)
        vector2=numpy.random.randint(1,200,z).tolist()
        print(vector2)
        
        print('\n')
        
        op=input('¿Qué operación desea realizar?: ')
        if op=="Suma" or op=='suma' or op=='SUMA':
            
            for i in range(0,z):
                vector3[i]=vector1[i]+vector2[i]
            for i in range(z):
                print(vector3[i], end=' ')
            print('\n')
        salir=input('¿Desea realizar otra operación?: ')
        if salir=="No" or salir=='NO' or salir== 'nO' or salir=='no':
            break
            
        if op=="Resta" or op=='resta' or op=='RESTA':
            
            for i in range(0,z):
                vector3[i]=vector1[i]+vector2[i]
            for i in range(z):
                print(vector3[i], end=' ')
            print('\n')
        salir=input('¿Desea realizar otra operación?: ')
        if salir=="No" or salir=='NO' or salir== 'nO' or salir=='no':
            break
        if op=="Multiplicacion" or op=='multiplicación' or op=='MULTIPLICACION':
            
            for i in range(0,z):
                vector3[i]=vector1[i]+vector2[i]
            for i in range(z):
                print(vector3[i], end=' ')
            
            print('\n')
        salir=input('¿Desea realizar otra operación?: ')
        if salir=="No" or salir=='NO' or salir== 'nO' or salir=='no':
            break
    
        if op=="División" or op=='division' or op=='División':
            
            for i in range(0,z):
                vector3[i]=vector1[i]+vector2[i]
            for i in range(z):
                print(vector3[i], end=' ')
            print('\n')
        salir=input('¿Desea realizar otra operación?: ')
        if salir=="No" or salir=='NO' or salir== 'nO' or salir=='no':
            break
            
print('\n')