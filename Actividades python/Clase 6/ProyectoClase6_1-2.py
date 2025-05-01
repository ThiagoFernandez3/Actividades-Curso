opciones=['Precio','Nombre','Stock']
precio=[]
nombre=[]
stock=[]
salir= False
indice=0

while salir == False:
    print('Ingrese el Precio, el Nombre y la cantidad de stock del producto.')
    nombre.append(input(f'{opciones[1]}: '))
    precio.append(float(input(f'{opciones[0]}: ')))
    stock.append(int(input(f'{opciones[2]}: ')))
    respuesta=input('Desea agregar mas productos?\n-')
    respuesta=respuesta.lower()
    if respuesta == 'si':
        indice=indice+1
        salir
    elif respuesta == 'no':
        ingreso= zip(precio, nombre, stock)
        INVENTARIO=tuple(ingreso)
        salir= True
        
for i in range(indice+1):
    print('-'*20)
    print(f'{opciones[1]}: {INVENTARIO[i][1]}.')
    print(f'{opciones[0]}: {INVENTARIO[i][0]}$.')
    print(f'Cantidad en {opciones[2]}: {INVENTARIO[i][2]}.')
            
            