# Una carrera tuvo 5 participantes. El resultado se representa con una tupla anidada,
# donde cada participante tiene su posición y tiempo en segundos.

# RESULTADOS = ((1, "Laura", 120), (2, "Carlos", 125), (3, "Ana", 130), (4, "Pedro", 140), (5, "Luis", 150))

# Instrucciones:
# -Define la tupla como se indica.
# -Encuentra al participante que llegó en tercer lugar.
# -Usa un método para verificar si "María" participó en la carrera.
# -Ordena la tupla por tiempos y muestra al ganador.
# -Pregunta extra: Cual es la diferencia entre el primero y el ultimo?

maria=  False
min_tiempo=0
RESULTADOS = ((1, "Laura", 120), (2, "Carlos", 125), (3, "Ana", 130), (4, "Pedro", 140), (5, "Luis", 150))
print(f'Tercer lugar: {RESULTADOS[2][1]}')

for i in range(len(RESULTADOS)):
    if RESULTADOS[i][1] == 'Maria':
        maria= True
    elif RESULTADOS[i][1] != 'Maria':
        maria

if maria == True:
    print('Maria participo.')
elif maria == False:
    print('Maria no participo.')
    

orden = list(RESULTADOS)
orden = sorted(orden, key=lambda x: x[2])
ganador= orden[0]
print(f'El ganador es {ganador[1]} con un tiempo de {ganador[2]}s.')

diferencia = orden[4][2] - orden[0][2]
print(f"La diferencia de tiempo entre el primero y el último es {diferencia} segundos.")
