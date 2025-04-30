# Objetivo:
# Crear un generador de contraseñas que permita practicar while, for con range, comprensión de listas,
# y el uso de break y continue.
# Descripción:
# • El programa genera contraseñas seguras con una longitud definida por el usuario.
# • La longitud debe ser mayor o igual a 8 (usa continue para validar).
# • Se pueden generar múltiples contraseñas hasta que el usuario decida salir (usa break).
# • Utiliza comprensión de listas para construir las contraseñas a partir de caracteres alfanuméricos y símbolos.
caracteres = [chr(i) for i in range(33, 127)]
contraseña=[]
while True:
    longitud= int(input('Cuanto quiere que mida la contraseña?(hasta 8)'))
    if longitud < 8:
        print('La longuitud minima es de 8.')
        continue
    
    contraseña = [caracteres[(i * 7 + 3) % len(caracteres)] for i in range(longitud)]
    print("Contraseña generada:", "".join(contraseña))
    opcion = input('quiere generar mas contrseñas? (s/n)').lower()
    if opcion != 's':
        print('FIn')
        break
    
   


