# Filtrando números pares
# Objetivo:
# Introducir la comprensión de listas y el uso de for con range.
# Descripción:
# • El programa genera una lista de números del 1 al 20 usando range.
# • Usa comprensión de listas para filtrar los números pares.
# • Permite a los estudiantes imprimir los números pares o detener el programa usando break.
 
lista=list(range(1,21))

pares=[numero for numero in lista if numero % 2 == 0]
print('numeros pares del 1 al 20.')
for num in pares:
    print(num)