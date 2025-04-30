# Generador de Frases

# Objetivo: Aplicar funciones con argumentos opcionales y con retorno.
# Instrucciones:

# Escribe una función llamada crear frase que reciba tres parámetros: sujeto, verbo y objeto.

# Si no se proporciona un objeto, deberá usar el valor por defecto "algo interesante".

# La función debe retornar una frase completa formada por los tres parámetros.

# Escribe otra función llamada imprimir frase que reciba la frase generada y la imprima en pantalla.

def crear_frase(a,b,c):
    frase = a + ' ' + b + ' '+ c
    return frase

def imprimir_frase(a):
    print(f'Su frase es: {a}')

sujeto= input('Ingrese el sujeto de la frase.\n')
verbo= input('Ingrese el verbo de la frase.\n')
respuesta= input('Quiere agregar un objeto(s/n)').lower()

if respuesta == 's':
    objeto= input('Ingrese el objeto de la frase.\n')
else:
    objeto= 'Algo interesante.'
    

imprimir_frase(crear_frase(sujeto,verbo,objeto))
