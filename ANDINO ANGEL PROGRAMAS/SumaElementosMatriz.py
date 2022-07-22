# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 11:49:36 2022

@author: Renato
"""
acu=0
A=[[2, 4, 5],[5, 6, 7]]
for i in range(len(A)):
    for j in range(len(A[i])):
        acu=acu+A[i][j]
print(acu)