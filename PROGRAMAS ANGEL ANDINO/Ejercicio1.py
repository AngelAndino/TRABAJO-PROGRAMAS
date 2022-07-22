# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 17:34:43 2022

@author: Renato
"""

print("    |",end="")
for i in range(1,5):
    print(i,end="\t")
print("      ",end="   ")
for i in range(1,25):   # línea horizontal
	print("-",end="")
#print()
for i in range(1,11):
 	print("\n",i*10,"|",end="\t\t")
 	for j in range (1,5):
	  print(round(j,1),end="    ")