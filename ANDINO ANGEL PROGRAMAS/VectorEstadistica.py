# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 12:36:10 2022

@author: Renato
"""
import math
t=int(input('Ingrese el tamaño del vector:'))
a=[]
for i in range(t):
    a.append([0])

for i in range(t):
    a[i]=int(input('Ingrese el elemento {}:'.format(i+1)))
 
def Media(vec,t):
    acu=0
    for i in range(t):
        acu=acu+vec[i]
    return (acu/t)

def Varianza(vec,t):
    acu=0
    for i in range(t):
        acu=float(acu+(vec[i]-Media(vec,t))**2)
    return (acu/t)


print("a:",a)
print('La media es:',Media(a,t))
print('La media es:',Varianza(a,t))
print('La desviación estándar es:',math.sqrt(Varianza(a,t)))




