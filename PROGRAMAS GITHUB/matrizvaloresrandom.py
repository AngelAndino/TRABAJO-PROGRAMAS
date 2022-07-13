# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 13:06:05 2022

@author: Dell
"""
from random import randint

m2=[0]*4
for i in range(4):
    m2[i]=[0]*4

for h in range (4):
    for y in range (4):
     t=randint(0,1000)
     m2[h][y]=t

for h in range (4):
    for y in range (4):
        print(m2[h][y],end=" ")
    print(" ")