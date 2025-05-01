# Análisis de encuestas

# Descripción: Un sistema de encuestas recopila calificaciones de satisfacción (del 1 al 10).
# Crea un programa que:

# -Filtre las calificaciones mayores o iguales a 7 (satisfacción alta).

# -Calcule el promedio de las calificaciones filtradas.

# -Devuelva un mensaje personalizado dependiendo del promedio:

#  Promedio < 9: "¡Excelente satisfacción general!"

#  Promedio entre 7 y 8.9: "Buena satisfacción general."

#  Promedio < 7: "Necesitamos mejorar."

# Objetivo:
# Usar filter, reduce, y callbacks para análisis de datos.

from random import randint

from functools import reduce
  
lista_satisfaccion = []

while len(lista_satisfaccion) <= 10: 
    lista_satisfaccion.append(randint(1,10))

calificacones_filtradas= list(filter(lambda satisfaccion: satisfaccion >= 7, lista_satisfaccion))

if len(calificacones_filtradas) > 1:
    
    promedio= reduce(lambda calificacion, calificacion1: calificacion + calificacion1, calificacones_filtradas)
    
    promedio= promedio / len(calificacones_filtradas)
    
    if promedio  >= 9:
        mensaje= '-Excelente satisfaccion general.'
        
    elif promedio > 7 and promedio <= 8.9:
        mensaje= '-Buena satisfaccion general.'
        
    else:
        mensaje= '-Necesitamos mejorar.'
else:
    
    promedio= reduce(lambda x, y: x + y, lista_satisfaccion)
    promedio= promedio/ len(lista_satisfaccion)
    mensaje= 'Necesitamos mejorar'
    
    
print(f'.Satisfaccion general: \n {lista_satisfaccion}')
print(f'-Calificacciones altas: \n {calificacones_filtradas}')
print(f'-Promedio de satisfaccion: \n {round(promedio,2)}')
print(f'{mensaje}')

    
