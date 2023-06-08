## Mostrar el desglose de un número usando la CONJETURA DE COLLATZ

numero = int(input("Introduce un número: "))
resultado = int(numero);

while numero > 1:

    if numero % 2 == 0:
        resultado = numero / 2
        print(int(numero), " / 2 = ", int(resultado))
        numero = resultado;

    elif numero % 2 != 0:
        resultado = (numero * 3) + 1
        print(int(numero), " * 3 + 1 = ", int(resultado))
        numero = resultado;


