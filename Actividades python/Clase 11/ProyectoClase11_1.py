# Analizador de compras online

# Descripción:
# Un sistema de e-commerce tiene una lista de precios de productos y desea:
# -Filtrar los productos que cuestan más de un valor mínimo ingresado por el usuario.
# -Aplicar un descuento del 10% a los productos seleccionados.
# -Calcular el costo total después del descuento.
# Objetivo:
# Resolver un problema realista usando las funciones vistas.
from functools import reduce

# Le pido los productos al usuario con un input, con split los separo por coma y guardo como una lista
productos = input('ingrese la listas de productos separados por coma.\n-').split(', ')

# Le pido lo mismo pero con los precios
lista_precios = input('Ahora, ingrese la lista de precios de esos productos en orden (separados por espacio)\n-')

# Aca tomo esos datos que estaban como str en y com map los haga a todos enteros, con split les saco el espacio  
lista_precios= list(map(int, lista_precios.split(' ')))

# Le pido al usuario el valor minimo y lo guardo en una variable como entero
valor_min = int(input('Cual es el valor minimo por el que se van a filtrar?\n-'))

# Comprimo la lista de productos y precio usando zip en una sola
lista_productos= list(zip(productos, lista_precios))

# Usando filter y lambda creo una lista de los productos que superen el precio minimo
lista_filtrada = list(filter(lambda precio: precio[1] >= valor_min, lista_productos))

# A la lista filtrada le aplico el descuento de 10% con lambda, lo redondeo a 2 decimales con round y lo guardo en una lista
lista_descuento = list(map(lambda x: (x[0], round(x[1] * 0.9, 2)), lista_filtrada))

# Sumo los precios usando reduce y guardo el total
total= reduce(lambda suma, PrecioProduct: suma + PrecioProduct[1], lista_descuento, 0)

# Con un for recorro la lista con descuento y imprimo el producto y el precio con el descuento
print('Productos con su descuento aplicado:')
for producto, precio in lista_descuento:
    print(f'- {producto}: ${precio}')

# Presento el total de lo descontado
print(f'Costo total despues del descuento: ${total}')