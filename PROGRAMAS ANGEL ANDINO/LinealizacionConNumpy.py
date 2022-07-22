# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 12:12:16 2022

@author: Renato
"""

import numpy as np
A=np.array([[2, 4, 5],[5, 6, 7],[4, 6, 7],[1, 0, 3],[3, 6, 1]])
#A=[[2,6,7,9,4,6,3],[3,6,2,5,8,2,5]]
print()
for i in A:
    print("[ ",end="")
    for j in i:
        print("{}".format(j),end=" ")
    print("]")
print() 

B=A.flatten()
C=A.flatten(order='F')
D=A.flatten(order='A')
print(B)
print(C)
print(D)