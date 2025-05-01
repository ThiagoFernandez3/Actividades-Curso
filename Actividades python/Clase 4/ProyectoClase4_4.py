# Club de lectura interactivo (if/elif y lógica)
# Formas parte de un club de lectura que clasifica libros según las preferencias de las lectoras:
# 1. Romance y finales felices: recomienda 'Orgullo y prejuicio'.
# 2. Aventuras y héroes valientes: sugiere 'Harry Potter'.
# 3. Misterios: elige 'Sherlock Holmes'.
# 4. Otro género: recomienda 'Explora nuevas historias'.
# Escribe un programa que tome la opción del usuario y muestre la recomendación correspondiente.

def recomendar_historias():
    respuesta=int(input('Que historias Prefiere?\n -1: Romance y finales felices\t -2: Aventuras y heroes valientes.\n -3: Misterio.\t\t\t -4: Otros.\n-'))
    if respuesta==1:
        print('Te recomiendo Orgullo y prejuicio.')
    elif respuesta==2:
        print('Te recomiendo Harry Potter.')
    elif respuesta==3:
        print('Te recomiendo Sherlock Holmes.')
    elif respuesta==4:
        print('Te recomiendo Explorar nuevas historias.')
        recomendar_historias()
    else:
        print('Ingrese la opcion correctamente.')
        recomendar_historias()
recomendar_historias()