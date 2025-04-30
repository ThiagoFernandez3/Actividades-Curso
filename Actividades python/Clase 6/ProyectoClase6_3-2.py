# Tupla con las temperaturas mínimas y máximas de la semana
TEMPERATURAS = ((12, 22), (15, 25), (11, 21), (10, 20), (14, 24), (13, 23), (9, 19))

# Lista de los días de la semana
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

# 1. Extraer las temperaturas máximas y contar cuántas veces aparece 22
maximas = [maxima for _, maxima in TEMPERATURAS]
dias_max_22 = maximas.count(22)

# 2. Día con la temperatura mínima más baja
dia_minima_baja = min(TEMPERATURAS, key=lambda x: x[0])
indice_min_baja = TEMPERATURAS.index(dia_minima_baja)
dia_minima_baja_nombre = dias_semana[indice_min_baja]

# 3. Día con la mayor diferencia entre la temperatura mínima y máxima
dia_max_diff = max(TEMPERATURAS, key=lambda x: x[1] - x[0])
indice_max_diff = TEMPERATURAS.index(dia_max_diff)
dia_max_diff_nombre = dias_semana[indice_max_diff]

# Mostrar los resultados
print(f'Días con temperatura máxima de 22 grados: {dias_max_22}')
print(f'Día con la temperatura mínima más baja: {dia_minima_baja_nombre} con {dia_minima_baja[0]} grados')
print(f'Día con la mayor diferencia de temperatura: {dia_max_diff_nombre} con una diferencia de {dia_max_diff[1] - dia_max_diff[0]} grados')
