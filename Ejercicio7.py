# 7. Solicita al usuario dos fechas del MISMO año e
# indica la CANTIDAD DE DÍAS que hay ENTRE ellas.

#################### SOLICITUD DE DATOS ###########################
print("Introduce una fecha con formato dd/mm/aaaa")
fecha1 = input()
fecha1 = fecha1.split("/")
print(fecha1)

print("Introduce OTRA fecha con formato dd/mm/aaaa")
fecha2 = input()
fecha2 = fecha2.split("/")
print(fecha2)

#################### LÓGICA #######################################

## AÑOS
if fecha1[2] < fecha2[2]:
    dias = (int(fecha2[2])-int(fecha1[2]))*365
    dias = (int(fecha2[1])-int(fecha1[1]))*30

elif fecha2[2] < fecha1[2]:
    dias = (int(fecha1[2])-int(fecha2[2]))*365
    dias = (int(fecha2[1])-int(fecha1[1]))*30

print(dias)