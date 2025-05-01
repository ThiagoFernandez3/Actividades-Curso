# Simulador de subasta con generador y decorador

# Objetivo:
# -Crear un generador que simule una subasta donde se reciben ofertas dinámicamente,
# y un decorador que valide que las ofertas sean mayores a la actual. 
from random import randint

def subasta(funcion):
    def wrapper(oferta_actual):
        
        print(f'-Abriendo subasta por el objeto n*{randint(100,999)}:\n-Oferta iniciada en:')
        print(f'${oferta_actual}')
        
        while True:
            nueva= int(input('Ingrese la nueva oferta.\n-'))
            oferta_actual= funcion(oferta_actual, nueva)
            
            respuesta= input('Desea salir? (si/no)\n-').lower()
            
            if respuesta =='si':
                break
            else:
                continue
        print(f'Objeto subastado por: ${oferta_actual}.')
        print('-termino la subasta.👋')
    return wrapper


@subasta
def comparar_ofertas(oferta_actual,oferta_nueva):
    
    if oferta_nueva > oferta_actual:
        print(f'Oferta recibida: ${oferta_nueva}')
        
        return oferta_nueva
    
    else:
        
        print(f'No supera la oferta actual de:{oferta_actual}')
        return oferta_actual
comparar_ofertas(100)
