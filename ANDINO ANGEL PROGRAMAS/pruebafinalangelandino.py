# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 21:11:35 2022

@author: Angel Andino
"""

import random
def validar(num):
	if num>=4 and num<=10:
		print("El valor ingresado es valido")
		return True
	else:
		print("El valor ingresado es invalido")
		return False
		
def rellenar(matriz,n):
	for k in range(n+1):
		matriz.append([])
		for m in range(n+1):
				if k==n:
					matriz[k].append(0)
				elif m==n:
					matriz[k].append(0)
				else:
					matriz[k].append(random.randint(0,100))
					
def totales(matriz,n):
	for k in range(n):
		suma=0
		for m in range(n):
			suma=suma+matriz[k][m]
		matriz[k][n]=round(suma/n,2)
	for k in range(n+1):
		suma=0
		for m in range(n+1):
			suma=suma+matriz[m][k]
		matriz[n][k]=round(suma/n,2)

def imprimir(matriz,n):
	for k in range(n+1):
		print(" ",end="")
		for m in range(n+1):
			if m==n:
				print("TOTAL",matriz[k][m],end="  ")
			elif k==n:
				print("TOTAL",matriz[k][m],end="  \t ")
			else:
				if matriz[k][m]<10:
					print(matriz[k][m],end="   \t\t  ")
				elif matriz[k][m]==100:
					print(matriz[k][m],end=" \t\t  ")
				else:
					print(matriz[k][m], end="\t  \t  ")
		print("")


n=int(input("Ingrese el valor de N que desea: "))
if validar(n)==True:
	matriz=[]
	rellenar(matriz,n)
	totales(matriz,n)
	imprimir(matriz,n)
	