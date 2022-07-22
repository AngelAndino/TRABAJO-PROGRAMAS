# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 12:21:18 2022

@author: Renato
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 23:10:04 2022

@author: Renato
"""

#Linealización
A=[[2, 4, 5],[5, 6, 7],[4, 6, 7]]
print('MATRIX')
for fila in A:
    print("[ ",end="")
    for elemento in fila:
        print("{}".format(elemento),end=" ")
    print("]")
print()        

vec=[]
t=len(A)*len(A[0])
#print(t)

for i in range(len(A)):
    for j in range(len(A[0])):
        val=A[j][i]
        vec.append(val)
        
print('Vector')
print(vec)