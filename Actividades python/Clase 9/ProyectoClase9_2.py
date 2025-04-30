# Ejercicio 2:
# Simulador de Ahorro Mensual

# Objetivo: Practicar funciones con parámetros, retorno y valores predeterminados.
# Instrucciones:
# Escribe una función llamada calcular ahorro que reciba como parámetros:
# ** monto mensual (cantidad ahorrada cada mes).
# ** meses (cantidad de meses, por defecto 12).
# ** La función debe retornarel total ahorrado.
# Escribe otra función llamada mostrar_ahorro que reciba el total ahorrado y lo imprima en pantalla (sin retorno).
# Crea un programa que permita al usuario ingresar el monto mensual y opcionalmente los meses.

def calcular_ahorro(a,b):
    total = a * b
    return total

def mostrar_ahorro(a,b):
    print(f'El monto ahorrado en {b} meses es: ${a}.')
    
monto_meses= int(input('Cuanto ahorra en un mes?.\n'))
respuesta=input('Quiere saber el monto ahorrado de un periodo de meses en especifico? (s/n)\n')
if respuesta == 's':
    meses= int(input('Cuantos meses quiere saber?'))
else:
    meses= 12
    
mostrar_ahorro(calcular_ahorro(monto_meses,meses),meses)


