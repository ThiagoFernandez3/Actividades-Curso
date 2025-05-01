# Ejercicio 1:
# Generador de Frases:
# Objetivo: Aplicar funciones con argumentos opcionales y con retorno.
# Instrucciones:
# Escribe una función llamada crear frase que reciba tres parámetros: sujeto, verbo y objeto.
# Si no se proporciona un objeto, deberá usar el valor por defecto "algo interesante".
# La función debe retornar una frase completa formada por los tres parámetros.
# Escribe otra función llamada imprimir frase que reciba la frase generada y la imprima en pantalla.

def crear_frase(a,b,c='Algo interesante'):
    d = a + ' ' + b + ' ' + c
    return d

def imprimir_frase(a):
    print(a)

sujeto= input('Ingrese el sujeto de la frase.\n-')
verbo= input('Ingrese el verbo.\n-')
respuesta= input('Quiere agregar un objeto?(s/n)\n-').lower()
if respuesta == 's':
    objeto= input('Ingrese el objeto.\n-')
    imprimir_frase(crear_frase(sujeto,verbo,objeto))
else:
    imprimir_frase(crear_frase(sujeto,verbo))


