# Símbolos de Divisas
# Instrucciones:

# Crea un diccionario llamado divisas con las siguientes claves y valores:
# • 'Euro': '€'
# • 'Dolar': 'S'
# • "Yen': 'Y"

# > Pide al usuario que ingrese el nombre de una divisa.
#   Busca en el diccionario si la divisa existe:
# • Si existe, muestra su símbolo.
# • Si no existe, muestra un mensaje indicando que la divisa no está en el diccionario.

divisas={'Euro': '€',
        'Dolar': '$',
        'Yen' : '¥' }
pregunta=input('-Ingrese el nombre de una divIsa:\n-')
if pregunta in divisas:
    print(f'-{divisas.get(pregunta)}')
else:
    print(f'-{divisas.get(pregunta, 'No esta disponible.')}')