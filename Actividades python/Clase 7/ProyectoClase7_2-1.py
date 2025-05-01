# instrucciones:
# Pide al usuario que ingrese dos listas de números separados por espacios.
# >Convierte cada lista en un conjunto para eliminar duplicados.
# >Calcula la intersección de los dos conjuntos para encontrar los elementos comunes.

# Muestra los elementos comunes encontrados.
# Ejemplo de Ejecución:

# Entrada del usuario:
# Lista 1: "1 2 3 4 5"
# Lista 2: "3 4 5 6 7"

# • Salida:
# • "Los elementos comunes son: {3, 4, 5}"

interseccion=[]

l1= input('Ingrese numeros para la primera lista (los numeros debreran estar separados por un espacio).\n-')
l2=input('Ingrese numeros para la segunda lista (los numeros debreran estar separados por un espacio).\n-')
l1= set(l1)
l2= set(l2)

l1.remove(' ')
l2.remove(' ')

for i in l1:
    for j in l2:
        if i == j:
           interseccion.append(i)
           
print(f'Los elementos comunes son: {interseccion}') 