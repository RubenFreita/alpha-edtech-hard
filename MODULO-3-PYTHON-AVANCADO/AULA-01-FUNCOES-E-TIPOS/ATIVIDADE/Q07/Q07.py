

def processar_numeros(a, b, callbak):

    return callbak(a,b)


def multiplica(a,b):
    return a*b


def soma(a,b):
    return a+b


numero1 = 5
numero2 = 9
print(f"A Soma de {numero1} e {numero2}:")
print(processar_numeros(numero1, numero2, soma))
print(f"A multiplicação de {numero1} por {numero2}:")
print(processar_numeros(numero1, numero2, multiplica))