

def calculadora(x, y, tipo="soma"):

    if tipo == "soma":
        return soma(x,y)
    elif tipo == 'produto':
        return produto(x, y)
    elif tipo == 'subtracao':
        return subtracao(x, y)
    elif tipo == 'divisao':
        return divisao(x, y)


def soma(x,y):
    return x+y
def produto(x,y):
    return x*y
def subtracao(x,y):
    return x-y
def divisao(x,y):
    return x/y

x = 4
y = 2

print(f"A soma de {x} e {y}: {calculadora(x,y)}")
print(f"O produto de {x} e {y}: {calculadora(x,y,tipo='produto')}")
print(f"A subtração de {x} e {y}: {calculadora(x,y,tipo='subtracao')}")
print(f"A divisão de {x} e {y}: {calculadora(x,y,tipo='divisao')}")
