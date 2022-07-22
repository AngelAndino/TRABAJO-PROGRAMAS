num1=int(input('Ingrese primer numero:'))
num2=int(input('Ingrese segundo numero:'))
num3=int(input('Ingrese tercer numero:'))
if num1>num2 & num2>num3:
    print(num1, ' ', num2, ' ', num3)
if num2>num1 & num1>num3:
    print(num2, ' ', num1, ' ', num3)
if num3>num2 & num2>num1:
    print(num3, ' ', num2, ' ', num1)