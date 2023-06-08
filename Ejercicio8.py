## CALCULAR DNI
## MÉTODO CORTO

dni = int(input("Introduce tu número de DNI: "))
numero = (dni%23)

letrasDNI = "TGPNQCRMDJVKWYXZHEAFBSLT"

print("Tu DNI completo es: ", dni,letrasDNI[numero-1])