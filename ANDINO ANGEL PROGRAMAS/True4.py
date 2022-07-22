# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:59:35 2022

@author: Renato
"""
i=1
cont1=0
acu1=0
cont2=0
acu2=0
while True:
    a=int(input('Ingrese Intervalo Inferior:'))
    b=int(input('Ingrese Intervalo Superior:'))
    if a!=b and a<b:
        cal=int(input('Ingrese la primer nota:'))
        if cal>=a and cal<=b:
            acu1=cal
            cont1=1
        else:
            acu2=cal
            cont2=1
        while cal!=0:
            cal=int(input('Ingrese notas:'))
            if cal>=a and cal<=b:
                acu1=acu1+cal
                cont1=cont1+1
            else:
                acu2=acu2+cal
                cont2=cont2+1 

        break      
print('La suma correctos es:',acu1)
print('La suma incorrectos es:',acu2)