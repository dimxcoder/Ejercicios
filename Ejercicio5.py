# Crea una variable que sea una letra,
# si es una A muestra el número 7,
# si es una B, el 9,
# si es una C el 101 y
# si NO es ninguno de los tres, indica que se han equivocado de letra

letra = input('Introduce una letra')
if letra == 'a':
    print(7)
elif letra == 'b':
    print(9)
elif letra == 'c':
    print(101)
elif letra != 'a' and letra != 'b' and letra != 'c':
    print('Te has equivocado de letra')

