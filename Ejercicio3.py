# 3. Suma o resta dos números reales
# Solicita la información al usuario

print('¿Qué operación desea realizar?')
print('1. Sumar')
print('2. Restar')

operacion = int(input())

n1 = int(input('Introduce un número'))
n2 = int(input('Introduce otro número'))

if operacion == 1:
    print(n1 + n2)
else:
    if operacion == 2:
       print(n1 - n2)