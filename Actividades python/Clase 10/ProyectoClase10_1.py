# Calculadora Básica
# Contexto: Vas a crear una función llamada calculadora basica que recibirá dos números y una operación matemática
# (suma, resta, multiplicación o división) como argumentos.
# La función debe:
# -Utilizar *args para manejar los dos números.
# -Utilizar **kwargs para especificar la operación matemática.
# -Incluir funciones anidadas para cada operación matemática.
# -Mostrar el resultado de la operación.

def calcudora_basica(*args,**kwargs):
    
    def suma(*args):
        resultadoSum= 0
        for i in args:
            resultadoSum += i
        return resultadoSum
    
    def resta(*args):
        resultadoRes= args[0]
        
        for i in args[1:]:
            resultadoRes -= i
        return resultadoRes
    
    def multiplicar(*args):
        resultadoMul= args[0]
        for i in args[1:]:
            resultadoMul *= i
        return resultadoMul
    
    def dividir(*args):
        resultadoDiv= args[0]
        for i in args[1:]:
            if i == 0 and resultadoDiv == 0:
                return "Error: División por cero"
            resultadoDiv /= i
        return resultadoDiv
    
    operacion = kwargs.get('operacion')
    
    if operacion == 'sumar':
        resultado= suma(*args)
    elif operacion == 'restar':
        resultado= resta(*args)
    elif operacion == 'multiplicar':
        resultado= multiplicar(*args)
    elif operacion == 'dividir':
        resultado= dividir(*args)
    else:
        print('No dio una operacion valida.')
    
    print(f'El resultado de {operacion} es: {resultado}')
    
salir= False
while salir== False:
    numeros= input('A que numeros quiere someter a las operaciones?(separados por espacio)\n-')
    numeros= list(map(int, numeros.split()))
    operaciones= input('Que operacion quiere hacerle a los numeros?(sumar, restar, multiplicar, dividir), si no quiere realizar ninguna escriba "salir".\n-').lower()
    if operaciones == 'salir':
        print('salir')
        salir=True    
    calcudora_basica(*numeros, operacion=operaciones)