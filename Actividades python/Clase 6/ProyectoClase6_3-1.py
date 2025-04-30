# Una agencia meteorológica lleva un registro de las temperaturas mínimas y máximas durante una semana.
# Cada día está representado por una tupla con dos valores (mínima, máxima).

# Instrucciones:
# -Define una tupla llamada TEMPERATURAS con los registros:
#  TEMPERATURAS = ((12, 22), (15, 25), (11, 21), (10, 20), (14, 24), (13, 23), (9, 19))
# -Usa un método para contar cuántos días tuvieron una temperatura máxima de 22 grados.
# -Encuentra el día con la temperatura mínima más baja.
# -Pregunta extra: ¿Qué día tuvo la mayor diferencia entre la temperatura mínima y máxima?

# Tupla con las temperaturas mínimas y máximas de la semana
TEMPERATURAS = ((12, 22), (15, 25), (11, 21), (10, 20), (14, 24), (13, 23), (9, 19))

semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

max22 = sum(1 for _, maxima in TEMPERATURAS if maxima == 22)

tempBaja = min(TEMPERATURAS, key=lambda x: x[0])

diferencia = max(TEMPERATURAS, key=lambda x: x[1] - x[0])

print(f'Día/s con temperatura máxima de 22 grados: {max22}')
print(f'Día con la temperatura mínima más baja fue {semana[TEMPERATURAS.index(tempBaja)]} con {tempBaja[0]} grados.')
print(f'Día con la mayor diferencia de temperatura fue el {semana[TEMPERATURAS.index(diferencia)]} con una diferencia de {diferencia[1] - diferencia[0]} grados. {diferencia}')
