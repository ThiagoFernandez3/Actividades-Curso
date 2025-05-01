# Ejercicio 1:

# Adivina el número
# Objetivo:
# Practicar el uso de while, break, y continue en un juego interactivo.
# Descripción:
# El programa genera un número aleatorio entre 1 y 10, se requiere adivinarlo.
# Si el número ingresado no está entre 1 y 10,
# el programa muestra un mensaje y utiliza continue para pedir un nuevo intento.
# Si adivinan correctamente, el programa usa break para terminar el bucle.
from random import randint
respuesta= 0
numero= 1
intentos=0
while respuesta != numero:
    numero= randint(1 ,10)
    respuesta= int(input('Adivine el numero. (1-10)\n'))
    intentos= intentos +1
    if respuesta > 10 and respuesta > 1:
        print('Vuleva a intentar.')
        respuesta= 0
        continue
    elif respuesta == numero:
        print(f'Le tomo {intentos} intentos.')
        break