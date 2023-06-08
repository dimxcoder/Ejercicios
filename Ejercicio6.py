# Dispones de tres números enteros
# H, M, S correspondientes a HORA, MINUTOS y SEGUNDOS respectivamente.
# Debes comprobar si se trata de una hora válida.
hora = int(input("Introduce la HORA"))
minutos = int(input("Introduce los MINUTOS"))
segundos = int(input("Introduce los SEGUNDOS"))

while hora < 0 or hora > 24:
    print("Has introducido una cifra de HORA incorrecta")
    print()
    hora = int(input("Introduce la HORA de nuevo"))
    print()

while minutos < 0 or minutos > 59:
    print("Has introducido una cifra de MINUTOS incorrecta")
    print()
    minutos = int(input("Introduce los MINUTOS de nuevo"))
    print()

while segundos < 0 or segundos > 59:
    print("Has introducido una cifra de SEGUNDOS incorrecta")
    print()
    segundos = int(input("Introduce los SEGUNDOS de nuevo"))
    print()

print("==================================")
print('La hora introducida es: ' + str(hora) + ":" + str(minutos) + ":" + str(segundos))
print("==================================")
