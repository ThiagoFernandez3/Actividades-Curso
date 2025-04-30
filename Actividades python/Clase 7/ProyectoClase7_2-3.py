interseccion=[]

l1= input('Ingrese numeros para la primera lista (los numeros debreran estar separados por un espacio).\n-')
l2=input('Ingrese numeros para la segunda lista (los numeros debreran estar separados por un espacio).\n-')
l1= set(map(int, l1.split()))
l2= set(map(int,l2.split()))

interseccion = l1 & l2
           
print(f'Los elementos comunes son: {interseccion}') 