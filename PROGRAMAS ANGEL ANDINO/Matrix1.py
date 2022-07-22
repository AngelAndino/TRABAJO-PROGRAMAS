a=int(input('Ingrese el número de filas:'))
b=int(input('Ingrese el número de columnas:'))
A=[]
for i in range(a):
    A.append([])
for i in range(a):
    for j in range(b):
        valor=int(input('Fila {},Columna {}:'.format(i+1, j+1)))
        A[i].append(valor)

print()
for fila in A:
    print("[ ",end="")
    for elemento in fila:
        print("{}".format(elemento),end=" ")
    print("]")
print()        
    