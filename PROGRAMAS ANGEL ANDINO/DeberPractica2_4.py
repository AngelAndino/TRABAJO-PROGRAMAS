# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 17:43:47 2022

@author: Renato
"""

a=int(input('Ingrese el número de filas:'))
b=int(input('Ingrese el número de columnas:'))
vec1=[]
vec2=[]
vec3=[]
for i in range(a):
    vec1.append([0])
    vec3.append([0])
for i in range(a):
    vec1[i]=int(input('Elemento fila{}: '.format(i+1)))
    
for i in range(b):
    vec2.append([0])
for i in range(b):
    vec2[i]=int(input('Elemento columna{}: '.format(i+1)))  
	
print("    ",end="")

for i in range(len(vec2)):
    print(vec2[i], end="    ")
print()

for i in range(a):
    for j in range(b):
        valor=vec1[i]*vec2[j]
        vec3[i].append(valor)
    print(vec1[i],vec3[i],end="    ")   
    print()
   
   
   

