# Concurso de talentos (Expresión ternaria)
# En un concurso de talentos las participantes obtienen puntajes de O a 100.
# • Si una participante tiene un puntaje de 85 o más, pasa a la final.
# • Si no, queda eliminada.
# Escribe un programa que, usando una expresión ternaria, evalúe el puntaje e imprima el mensaje correspondiente.
puntaje= int(input('ingrese su puntaje.\n-'))

final= 'Felicidades, Estas en la final.' if puntaje >= 85 else 'Mala suerte, Quedaste eliminada.'
print(final)