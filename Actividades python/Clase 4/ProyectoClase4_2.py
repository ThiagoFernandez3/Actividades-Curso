# La detective lógica (and, or, not)
# Eres una detective resolviendo un caso. Tienes pistas sobre un robo y debes identificar
# si el sospechoso es culpable. 
# El programa debe evaluar las condiciones lógicas basándose en estas pistas:
# - Si el sospechoso estuvo en el lugar del robo y no tiene coartada válida, es culpable.
# - Si el sospechoso no estuvo en el lugar del robo, pero tiene objetos robados, también es culpable.
# - Si ninguna de las condiciones anteriores se cumple, es inocente.
# Usa and, or, y not para determinar si el sospechoso es culpable o inocente.
'''
hola
'''
culpable= False
print('Responda con un si o no a las preguntas para dar el veredicto.')
lugar=input('El Sospechoso estuvo en el lugar del robo?.\n-')
coartada=input('El sospechoso tiene una coartada?.\n-')
objetos=input('El sospechosos tenia objetos robados?.\n-')
if lugar=='si' or lugar=='Si' and coartada=='no' or coartada=='No':
    culpable= True
elif lugar=='no' or lugar=='No' or objetos=='si' or objetos=='Si':
    culpable== True
else:
    culpable
    
if  culpable== True:
    print('El sospechoso es culpable.')
else:
    print('El sospechoso es inocente.')
