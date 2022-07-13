# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 13:12:03 2022

@author: Angel Andino
"""

import random
import time

p=int(input("Ingrese el tamaño que desea en su vector : "))
vec=[0]*p
for i in range(p):
    a=random.randint(50, 100)
    vec[i]=a

print("El vector original es: ")
for i in range(p):
    print("el valor que se encuentra en la posición ",i+1,"es:",vec[i])
    time.sleep(1)

for i in range(1, p):
    for m in range(0, p - i):
        if (vec[m + 1] < vec[m]):
            aux = vec[m];
            vec[m] = vec[m + 1];
            vec[m + 1] = aux;

print("El vector ordenado es: ")
for i in range(p):
    print("el valor que se encuentra en la posición",i+1,"es:",vec[i])
    time.sleep(1)