# 2. Dispones de una frase y una letra,
# solicitados al usuario y
# debes mostrar la cantidad de veces
# que aparece la letra en la frase.

frase = input('Inserta una frase')
letra = input('Inserta una letra')
contador = 0

for i in frase:
    if i==letra:
        contador += 1

print("La letra " + str(letra) + " aparece " + str(contador) + " veces.")



