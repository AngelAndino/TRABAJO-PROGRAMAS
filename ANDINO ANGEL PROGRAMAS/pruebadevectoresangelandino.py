# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 20:36:37 2022

@author: Angel Andino 
"""

import random
def validar(num):
	if num>=4 and num<=30:
		print("El valor ingresado es válido")
		return True
	else:
		print("El valor ingresado es invalido")
		return False
		
def rellenar(vector,n,vprimos):
	k=0
	m=0
	for k in range (n-1):
		vector.append(random.randint(1,40))
	print("El vector es: ")
	for m in range (n):
		print(vector[m])
		if primo(vector[m])==True:
			vprimos.append(vector[m])

def primo(num):
	for n in range(2,num):
		if num%n == 0:
			return False
	return True
	
	
n=int(input("Ingrese el valor: "))
if validar(n)==True:
	primos=[]
	vector=[n]
	rellenar(vector,n,primos)
	if len(primos)==0:
		print("No existe ningún número primo")
	else:
		k=0
		print("Los numeros primos son: ")
		for k in range(len(primos)):
			print(primos[k],end=" ")