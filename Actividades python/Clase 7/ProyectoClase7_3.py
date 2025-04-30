# Buscador de Palabras Clave
# Instrucciones:
# > Imagina que tienes un texto (como si fuera una página web) 
# y necesitas identificar si ciertas palabras clave que aparecen en él.

# Tips:
# • Pide al usuario que ingrese un texto (puede ser una frase o párrafo corto).
# • Pide al usuario que ingrese una lista de palabras clave separadas por espacios.
# • Convierte las palabras del texto en un conjunto para obtener las palabras únicas.
# • Recorre la lista de palabras clave y verifica si están en el conjunto del texto.
# • Guarda el resultado en un diccionario con la palabra clave como clave y "Sí" o "No" como valor.
# • Muestra el diccionario resultante.

diccionario= {}
txt= (input('Escriba el texto.\n-')).lower()
clave= (input('Ingrese las palabras claves.\n')).lower()
txt= set(txt.split())
clave= (clave.split())
for c in clave:
    if c in txt:
        diccionario[c] = 'Si'
    elif c not in txt:
        diccionario[c] = 'No'
print("Palabras clave:")
for clave, valor in diccionario.items():
    print(f"-{clave}: {valor}")