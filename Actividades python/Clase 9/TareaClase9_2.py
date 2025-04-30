# Simulador de Ahorro Mensual

# Objetivo: Practicar funciones con parámetros, retorno y valores predeterminados.

# Instrucciones:

# Escribe una función llamada calcular ahorro que reciba como parámetros:
# ** monto mensual (cantidad ahorrada cada mes).
# ** meses (cantidad de meses, por defecto 12).
# ** La función debe retornar el total ahorrado.

# Escribe otra función llamada mostrar_ahorro que reciba el total ahorrado y lo imprima en pantalla (sin retorno).

# Crea un programa que permita al usuario ingresar el monto mensual y opcionalmente los meses.

def calcular_ahorro(a,b):
    total_ahorrado= a *b
    return total_ahorrado

def mostrar_ahorro(a,b):
    print(f'Su total ahorrado en {b} meses es de: ${a}.')
    
monto_mensual= int(input('Cuanto ahorra por mes?\n'))
pregunta = input('Quiere saber cuanto ahorro en cierta cantidad de meses?(s/n)(Si no se tomaran los ahorro de 12 meses.)\n')
if pregunta=='s':
    meses=int(input('Ingrese la cantidad de meses.\n'))
else:
    meses=12

mostrar_ahorro(calcular_ahorro(monto_mensual,meses),meses)