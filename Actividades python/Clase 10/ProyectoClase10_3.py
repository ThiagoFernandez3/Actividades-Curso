# Pizza Perfecta
# Contexto: Son chefs en una pizzería que permite a los clientes personalizar sus pizzas.
# Deben crear un sistema para calcular el precio de una pizza con ingredientes personalizados.
# Actividad:
# Escribe una función hacer_pizza(base, *ingredientes, **extras) que:
# Reciba el tipo de base ("fina", "gruesa").
# Reciba una lista de ingredientes principales como *args.
# Reciba extras opcionales como **kwargs ("queso_extra", "salsa_bbq").
# Calcule el precio final
# Cada ingrediente cuesta $500.
# Los extras tienen precios definidos en **kwargs.
def hacer_pizza(base, *ingredientes, **extras):
    precioBase = 2000 if base == 'gruesa' else 1500
    precioIng = 500 * len(ingredientes)
    precioExt = sum(extras.values())
    total = precioBase + precioIng + precioExt
    print('-'*35)
    print('-Recibo del pedido de pizza:')
    
    print(f'-Base: {base} (${precioBase}) ')
    print(f'-Ingredientes: {':($500), '.join(ingredientes)}:($500). Total Ingredientes:(${precioIng})')
    
    print(f'-Extras: {', '.join([f'{clave} (${valor})' for clave, valor in extras.items()])}')
    
    print(f'-Precio total: ${total}')
    print('-'*35)

base = input('● Como quiere que sea la masa de su pizza?\n-Fina ($1500) -Gruesa ($2000)\n-').lower()
ingrediente =input('● Que ingrediente quiere en su pizza? (cada uno cuesta $500)\n-').lower()
ingredientes = ingrediente.split(', ')
extras = {}

print('● Desea agregar alguno de los siguientes extras?\n-1. Queso extra ($250)\n-2. Salsa BBQ ($500)\n-3. Otro ($350)\n-4. Ninguno')

opExtra = input("●Escriba los números de los extras que desea, separados por coma.\n-").strip()

if opExtra:
    seleccion = [op.strip() for op in opExtra.split(',')]
    if '1' in seleccion:
        extras['queso_extra'] = 250
    if '2' in seleccion:
        extras['salsa_bbq'] = 500
    if '3' in seleccion:
        extras['otro'] = 350
    if '4' in seleccion:
        extras['ninguno']= 0
        
hacer_pizza(base,*ingredientes,**extras)