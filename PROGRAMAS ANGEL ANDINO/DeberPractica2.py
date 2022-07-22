# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 13:48:17 2022

@author: Renato
"""

n=t=0	#inicializo las variables '''
while t<=0:
	t=int(input("Ingrese el número de filas: "))
while n<=0:
	n=int(input("Ingrese el número de columnas: "))

for i in range(1,t+1):   # filas
	for j in range(1,n+1): #columnas
            ele=int(input(f"Ingrese el elemento ({i},{j}):"))
