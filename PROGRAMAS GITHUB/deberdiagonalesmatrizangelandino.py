# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 12:43:06 2022

@author: Dell
"""

import random 
while True:
    filas=int(input('Ingrese el numero de filas: '))
    columnas=int(input('Ingrese el numero de columnas: '))
    if filas<4 or columnas<4:
        print('Error las filas y columnas no pueden ser menor que 4')
    elif filas>30 or columnas>30:
        print('Error las filas y columnas no pueden ser mayor que 30')
    else:
     break
    
matriz=[[int()for i in range(filas)] for j in range(columnas)]
for i in range(filas):
    for j in range(columnas):
        matriz[i][j]=random.randint(50, 1000)

for i in range (filas):
    for j in range (columnas):
        print('|', matriz[i][j], '|', end=' ')
    print('   ')

if filas==columnas:
    print("La diagonal principal de la matriz  es: ")
    print()
    
    for i in range (filas):
     for j in range (columnas):
         if i==j:
          
          print("|",matriz[i][j],"|",end=" ")
         else:
          print("|","- ","|",end=" ")
     print(" ")
print()        
if filas==columnas:
 print("La diagonal secundaria de la matriz  es: ")
 print()
 
 for i in range (filas):
     for j in range (columnas):
      if i+j==filas-1:
       print("|",matriz[i][j],"|",end="  ")
      else:
       print("|","- ","|",end=" ")
     print(" ")