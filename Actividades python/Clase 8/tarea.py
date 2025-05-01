# Lista de caracteres permitidos (ASCII 33 al 126)
caracteres = [chr(i) for i in range(33, 127)]

# Inicio del bucle principal
while True:
    longitud = int(input("Ingrese la longitud de la contraseña (mínimo 8): "))

    if longitud < 8:
        print("La longitud mínima es 8. Intente nuevamente.")
        continue  # Vuelve a pedir la longitud

    # Generar la contraseña
    # Simulamos aleatoriedad eligiendo índices con una fórmula simple sin random
    contraseña = [caracteres[(i * 7 + 3) % len(caracteres)] for i in range(longitud)]
    print("Contraseña generada:", "".join(contraseña))

    # Preguntar al usuario si desea generar otra
    opcion = input("¿Desea generar otra contraseña? (s/n): ").lower()
    if opcion != 's':
        print("Fin del programa.")
        break