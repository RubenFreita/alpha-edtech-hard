

def soma_argumentos_nomeados(**argumentos):
    return sum(argumentos.values())


resultado1 = soma_argumentos_nomeados(a=10, b=20, c=30)
print(resultado1)

resultado2 = soma_argumentos_nomeados(a=10, b=20, c=30, d=40)
print(resultado2)