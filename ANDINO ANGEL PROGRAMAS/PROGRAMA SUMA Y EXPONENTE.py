# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 11:14:15 2022

@author: Dell
"""

n=int(input('Ingrese n: '))
sum=0
for i in range(1,n+1):
    sum=sum+pow(2,i)
print('La suma total es:',sum)