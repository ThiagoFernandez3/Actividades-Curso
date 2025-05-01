# Constructor de Universos
# Contexto: Son creadoras de universos y deben diseñar galaxias, estrellas y planetas.
# Cada universo tiene características únicas que deben ser configuradas usando *args y **kwargs.
# Además,una función anidada calcula el total de cuerpos celestes creados.
# Actividad:
# Diseña una función crear_universo(*galaxias, **configuracion) que:
# Use *args para recibir nombres de galaxias.
# Use **kwargs para configurar detalles como el número de estrellas y planetas por galaxia.
# Incluya una función anidada calcular_cuerpos() que calcule el total de cuerpos celestes creados en el universo.


def crear_universos(*galaxias, **configuracion):
    estrellas_galaxias= configuracion.get('estrellas_galaxias',0)
    planetas_galaxias = configuracion.get('planetas_galaxias',0)
    def calcular_cuerpos():
        total_estrellas= len(galaxias) * estrellas_galaxias
        total_planetas= len(galaxias) * planetas_galaxias
        return total_estrellas + total_planetas
    
    print('Universo creado con las siguientes galaxias:')
    for galaxia in galaxias:
        print(f'-{galaxia.strip()}.')
        
    print(f'Cada galaxia contiene {estrellas_galaxias} estrellas y {planetas_galaxias} planetas.')
    total = calcular_cuerpos()
    print(f'Las galaxias tienen {total} cuerpos celestes.')
    
nombreGalaxias= input('Ingrese el nombre de las galaxias a crear (separados por coma).\n-')

galaxias= nombreGalaxias.split(',')

estrellas = int(input('¿Cuántas estrellas tiene cada galaxia?\n-'))
planetas = int(input('¿Cuántos planetas tiene cada galaxia?\n-'))

crear_universos(*galaxias, estrellas_galaxias=estrellas, planetas_galaxias=planetas)