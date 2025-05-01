temperatura=int(input('Que temperatura hace actualmente?\n-'))
sol=input('Esta soleado afuera?\nResponde con si o no.\n-')
clima= 'Considera agregar gafas de sol en tu outfit.' if sol=='si' or 'Si' else 'Podrias llevar un paraguas.'
if temperatura > 30:
    print('Hace calor, le recomiendo ropa ligera y colorida.')
elif temperatura >= 20 and temperatura <=30:
    print('Esta algo fresco, te recomiendo ropa algo casual y comodo.')
elif temperatura < 20:
    print('Esta haciendo frio, te recomiendo que uses abrigos y bufandas')
print(clima)