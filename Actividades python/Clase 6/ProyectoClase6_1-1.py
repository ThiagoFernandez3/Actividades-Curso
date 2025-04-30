# Registro dinámico de inventario:
# Una tienda necesita registrar su inventario de productos. Cada producto debe incluir el nombre,
# precio y cantidad en stock.
# Los datos se almacenarán en una tupla anidada.

# Instrucciones:
# -Crea un programa que permita al usuario agregar productos al inventario.
# -Cada producto se representará como una tupla (nombre, precio, cantidad).
# -El programa debe preguntar al usuario si desea agregar más productos. Si responde "No",
#  debe salir de la interacción y mostrar el inventario actual.
# -Usa un bucle para permitir el ingreso dinámico de productos y almacénalos en una tupla.

opciones=['Precio','Nombre','Stock']
ingreso=[]
salir= False
indice=0
while salir== False:
    ingreso.append([])
    print('Ingrese el Precio, el Nombre y la cantidad de stock del producto.')
    for i in range(len(opciones)):
        ingreso[indice].append((input(f'{opciones[i]}: ')))
        
        
    respuesta=input('Desea agregar mas productos?\n-')
    respuesta=respuesta.lower()
        
    if respuesta == 'si':
         indice=indice+1
         salir
    elif respuesta == 'no':
        INVENTARIO=tuple(ingreso)
        for i in range(indice+1):
            print('-'*10)
            print(f'{opciones[1]}: {INVENTARIO[i][1]}.')
            print(f'{opciones[0]}: {INVENTARIO[i][0]}$.')
            print(f'Cantidad en {opciones[2]}: {INVENTARIO[i][2]}.')
            print('\n')
        salir=True


