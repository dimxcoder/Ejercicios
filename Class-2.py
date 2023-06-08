print("--------------TABLA DE MULTIPLICAR------------")

mult=int(input("Introduzca un número:"))
imprimir=""
for i in range(1,11):
    imprimir +=  str(mult*i)

print(f"Resultado Tabla {imprimir} ")