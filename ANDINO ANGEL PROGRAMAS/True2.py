# -*- coding: utf-8 -*-
"""
Created on Mon May 30 09:55:45 2022

@author: Renato
"""
a=int(input('Ingrese Intervalo Inferior:'))
b=int(input('Ingrese Intervalo Superior:'))
i=0
cont1=0
acu1=0
cont2=0
acu2=0
while True:
    cal=int(input('Ingrese la Calificación:'))
    i+=1
    if cal>a and cal<b:
        acu1=acu1+cal      
        cont1=cont1+1
    else:
        acu2=acu2+cal      
        cont2=cont2+1
    if cal == 0:
      break
print('La suma correctos es:',acu1)
print('La suma incorrectos es:',acu2)
