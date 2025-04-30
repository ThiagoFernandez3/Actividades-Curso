# Juego de Dados con Callbacks y Lambdas

# Objetivo:
# -Crear un juego de dados donde el jugador lanza dos dados y se suman sus resultados,
# usando funciones callback para comportamientos basados en los resultados y lambdas para simplificar el código.
# Instrucciones:
# -Función para lanzar dados:
# Crea lanzar dados que simule el lanzamiento de dos dados (números aleatorios entre 1 y 6) y devuelva sus resultados.
# 
# Comportamientos:
# -callback ganar: Si la suma es 7, imprime "¡Ganaste!".
# -callback perder: Si la suma es 2 o 12, imprime "Perdiste…".
# -callback_retirar: Si la suma es 3, 4, 5, 9, 10 u 11, imprime "Puedes retirar tu apuesta.".

# Función para jugar:
# Crea jugar que acepte una función callback, lance los dados y ejecute la callback con los resultados.
# Lambdas:
# callback_dobles: Si los dos dados son iguales, imprime "¡Dobles!".

from random import randint

print('Lanzando dados.')

def lanzar_dados():
    dados=[]
    for i in range(2):
        dados.append(randint(1,6))
    return dados

def callback_1(suma):
    print('-Ganaste') 

def callback_2(suma):
    print('-Pediste.')

def callback_3(suma):
    print('-Puedes retirar la suma.')
    
def jugar(funcion):
    dados= lanzar_dados()
    suma = sum(dados)
    
    print(f'-Resultados: {dados[0]} + {dados[1]}\n-Suma: {suma}')
    
    funcion(suma)
    
    dobles= lambda x,y: print('-Dobles.') if x==y else None
    dobles(dados[0],dados[1])

def resultado(suma):
    if suma==7:
        callback_1(suma)
    elif suma == 2 or suma == 12:
        callback_2(suma)
    elif suma in [3,4,5,9,10,11]:
        callback_3(suma)

jugar(resultado)



