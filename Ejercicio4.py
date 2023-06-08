# 4. Permite validar a un usuario con 3 intentos
# y los datos de validación correctos
# almacenados en dos constantes predefinidas.
USUARIO = 'usuario'
CONTRASEÑA = 'contraseña'

usuario = input("Introduce tu usuario")
contraseña = input("Introduce tu contraseña")

intento = 0;

while intento < 3:

    intento += 1

    if intento == 3:
        print('Espera 5 minutos y vuelve a intentarlo')
        break
    if usuario == USUARIO and contraseña == CONTRASEÑA:
        print('Datos correctos.')
        break

    elif usuario != USUARIO or contraseña != CONTRASEÑA:
        print('Vuelve a intentarlo.')
        usuario = input("Introduce tu usuario")
        contraseña = input("Introduce tu contraseña")