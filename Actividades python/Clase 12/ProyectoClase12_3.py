# Generador de tickets de soporte técnico con priorización

# Objetivo:
# - Diseñar un sistema que genere tickets de soporte técnico en tiempo real 
# y un decorador que asigne una prioridad basada en la descripción del problema.

from random import randint

grave=['caido','no funciona', 'error','urgente']
media=['lento','problema','demora','lenta']

def generar_tickets(funcion):
    def wrapper():
        print('Servivio de soporte: \n')
        
        problema= input('Cual es su problema?\n-').lower()
        
        funcion(problema)
        
        print(f'Su ticket a sido enviado✅.\nNumero de ticket: {randint(100,999)}\n')
        
    return wrapper


@generar_tickets
def asignar_prioridad(problema):
    
    if any(palabra in problema for palabra in grave):
        print('🔴Prioridad alta: Un tecnico se comunicara con usted en breve, porfavor espere.')
        
    elif any(palabra in problema for palabra in media):
        print('🟠Prioridad media: Intente reiniciar dispositivo, si el problema persiste un tecnico se conectara con usted.')
        
    else:
        print('🟢Prioridad baja: Puede que haya demora en solucionar su problema.')
        
asignar_prioridad()