# Decorador de superpoderes
# Objetivo: Crear un decorador que otorgue superpoderes a personajes de videojuegos
# y les permita realizar acciones especiales.

def superpoderes(poderes):
    def wrapper(poder):
        
        input('Otorgando poderes...')
        
        poderes(poder)
        
        print('Un gran poder conlleva una gran responsabilidad 🕷')
        
    return wrapper
   
@superpoderes
def otorgar_poderes(poder):
    print(f'-Eligio "{poder}"')
    
poder =(input('Que poder quiere?\n-'))

otorgar_poderes(poder)