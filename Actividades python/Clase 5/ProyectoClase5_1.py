# Organizador de tareas
# Crea un programa que permita al usuario agregar tareas a una lista y mostrarlas cuando lo desee.
# El programa ofrecerá tres opciones principales:
# **agregar tarea, ver todas las tareas y salir.
# El programa termina cuando el usuario elige salir.
print('1 - Agregar tarea\n2 - Ver todas las tareas\n3 - Salir')
tareas=[]
salir=False
while salir== False:
    respuesta=int(input('\nElige una opcion (1-3): '))
    if respuesta== 1:
        if tareas== None:
            tareas=[input('Escribe el nombre de la nueva tarea: ')]
        else:
            tareas.append(input('Escribe el nombre de la nueva tarea: '))
    elif respuesta==2:
        print('Tareas:')
        print('-','\n- '.join(tareas))
    elif respuesta==3:
        print('¡Hasta luego!')
        salir=True