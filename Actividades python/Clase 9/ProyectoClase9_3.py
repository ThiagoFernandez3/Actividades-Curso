# Ejercicio 3:
# Organizador de Eventos:
# Objetivo: Usar funciones con parámetros y retorno para planificar un evento y calcular los costos.
# Instrucciones:
# Crea una función llamada calcular_costo que reciba como parámetros:
# ** num personas (número de asistentes).
# **costo por persona (costo por persona, con valor predeterminado de 1000).
# ** Retorne el costo total del evento.
# Crea otra función llamada crear_resumen que reciba:
# ** nombre_evento (nombre del evento).
# ** num personas (número de asistentes).
# ** costo total (resultado de la función anterior).
# ** Retorne un resumen del evento como una cadena de texto.
# Crea una función llamada mostrar_resumen que reciba el resumen del evento y lo imprima (sin retorno).
# Diseña un programa que solicite al usuario los datos del evento y muestre el resumen final.

nombre_evento=str(input('Cual es el nombre del evento?\n'))
num_personas= int(input('Cuantas personas van a asistir al evento?\n'))
costo_per= int(input('Cual es el costo por persona?\n'))

def calcular_costo(a,b=1000):
    total= a*b
    return total

def crear_resumen(a,b,c):
    d= f'Nombre del evento:\n{a}\n-Numero de asistentes:\n{b}\n-Costo del evento:\n${c}'  
    return d
def mostrar_resumen(a):
    print(a)

mostrar_resumen(crear_resumen(nombre_evento,num_personas,(calcular_costo(num_personas,costo_per))))