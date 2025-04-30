# La diseñadora de outfits (if/elif y ternarios)
# Imagina que eres una diseñadora de moda virtual. 
# Escribe un programa que recomiende un outfit basado en las condiciones del clima:
# 1.Si hace calor (temperatura > 30), recomienda ropa ligera y colorida.
# 2.Si está fresco (20 <= temperatura <= 30), sugiere algo casual y cómodo.
# 3.Si hace frío (temperatura < 20), propone abrigos y bufandas.
# Extiende el programa usando una expresión ternaria para
# incluir un accesorio adicional:
# Si hace sol (sol == True), agrega gafas de sol al outfit.
# •Si no, sugiere llevar un paraguas.
# No te olvides de incorporar input()

def recomendar_ropa():
    temperatura=int(input('Que temperatura hace actualmente?\n-'))
    sol=input('Esta soleado afuera?\nResponde con si o no.\n-')
    clima= 'Considera agregar gafas de sol en tu outfit.' if sol=='si' or 'Si' else 'Podrias llevar un paraguas.'
    if temperatura > 30:
        print('Hace calor, le recomiendo ropa ligera y colorida.')
    elif temperatura <= 20 and temperatura <=30:
        print('Esta algo fresco, te recomiendo ropa algo casual y comodo.')
    elif temperatura < 20:
        print('Esta haciendo frio, te recomiendo que uses abrigos y bufandas')
    print(clima)

# La detective lógica (and, or, not)
# Eres una detective resolviendo un caso. Tienes pistas sobre un robo y debes identificar
# si el sospechoso es culpable. El programa debe evaluar las condiciones lógicas basándose en estas pistas:
# - Si el sospechoso estuvo en el lugar del robo y no tiene coartada válida, es culpable.
# - Si el sospechoso no estuvo en el lugar del robo, pero tiene objetos robados, también es culpable.
# - Si ninguna de las condiciones anteriores se cumple, es inocente.
# Usa and, or, y not para determinar si el sospechoso es culpable o inocente.

def resolver_misterio():
    culpable= False
    print('Responda con un si o no')
    lugar=input('El Sospechoso estuvo en el lugar del robo?.\n-')
    coartada=input('El sospechoso tiene una coartada?.\n-')
    objetos=input('El sospechosos tenia objetos robados?.\n-')
    if lugar=='si' or lugar=='Si' and coartada=='no' or coartada=='No':
        culpable= True
    elif lugar=='no' or lugar=='No' and objetos=='si' or objetos=='Si':
        culpable== True
    else:
        culpable
    if culpable== True:
        print('El sospechoso es culpable.')
    else:
        print('El sospechoso es inocente.')

respuesta=int(input('A que programa quiere acceder?.\n -1:Recomendar outfit.\t -2:Resolver Misterio.\n-'))
if respuesta==1:
    recomendar_ropa()
elif respuesta==2:
    resolver_misterio()