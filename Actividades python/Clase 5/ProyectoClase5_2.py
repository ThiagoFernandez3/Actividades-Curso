# Consultar el stock de productos
# Tu programa debe permitir al usuario consultar el inventario de una tienda
# para verificar si un producto está en stock.
# Si el producto está en la lista, el programa debe informarlo;
# si no, debe mostrar un mensaje indicando que no está disponible.
# Tips:
# • Usá una lista para almacenar los productos en stock.
# • Permite que el usuario ingrese el nombre de un producto a consultar.
# • Recorré la lista con un bucle "for" para verificar si el producto está en stock.

#inventario=['huevos','leche','harina','azucar','harina']

salir= False
printeado=0
inventario=[]
while salir== False:
    print('Que desea hacer?.')
    respuesta=int(input('1- Agregar productos al inventario.\n2- Comprobar Stock de un producto.\n3- Salir.\n'))
    if respuesta== 1:
        if inventario== None:
            inventario=[input('Que producto desea añadir al inventario?: ')]
        else:
            inventario.append(input('Que producto desea añadir al inventario?: '))
    elif respuesta== 2:
        if inventario== None:
            print('Añadi algo al inventario antes.')
        else:
            producto=input('Que producto quiere comprovar el stock?\n')
            productoMinus= producto.lower()
            for i in range(len(inventario)):
                if inventario[i]==productoMinus and printeado==0:
                    print(f'Hay stock de {productoMinus}.')
                    printeado= 1
                elif inventario.count(productoMinus)== 0 and printeado==0:
                    print(f'No hay stock de {productoMinus}.')
                    printeado= 1
    elif respuesta== 3:
        salir=True
        print('Adios.')