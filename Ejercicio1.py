# 1. Indicar cuál es el menor de tres números solicitados al usuario
n1 = input('Introduce el primer número')
n2 = input('Introduce el segundo número')
n3 = input('Introduce el tercer número')

if n1 < n2 and n1 < n3:
    print(str(n1) + ' es el menor de los tres número.')
else:
    if n2 < n1 and n2 < n3:
        print(str(n2) + ' es el menor de los tres número.')
    else:
        if n3 < n1 and n3 < n2:
            print(str(n3) + ' es el menor de los tres número.')
