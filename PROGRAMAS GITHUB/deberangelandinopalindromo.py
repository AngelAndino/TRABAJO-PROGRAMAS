# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 23:27:27 2022

@author: Angel Andino
"""

num = input("Ingrese el número que desea evaluar: ")
def palindromo(num):
    inicio = 0
    fin = len(num) - 1
    while num[inicio] == num[fin]:
        if inicio >= fin:
            print('Es palindromo')
            return True
        else: 
            inicio += 1
            fin -= 1
    print('No es palindromo')
    return False
print(palindromo(num))