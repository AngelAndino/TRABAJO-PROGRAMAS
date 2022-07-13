# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 11:07:16 2022

@author: Dell
"""
a=[1,2,3,4,5,6,7,8,9,10]
b=[1,2,3,4,5,6,7,8,9,10]
r=[0]*10

for h in range (0,10):
   r[h]=a[h]+b[h]

for h in range (0,10):
    print(r[h],end=" ")