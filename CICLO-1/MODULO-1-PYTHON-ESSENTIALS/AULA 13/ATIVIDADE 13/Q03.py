
#soma inteiros iterativa
# def soma_inteiros(n):
#     soma = 0
#     for i in str(n):
#         soma += int(i)
#     return soma

#soma inteiros recursiva
def soma_inteiros(n):
    if len(str(n)) == 1:
        return n
    return n%10 + soma_inteiros(n//10)



numero = 12345
print(f"A soma do número {numero} é {soma_inteiros(numero)}")
numero = 434567
print(f"A soma do número {numero} é {soma_inteiros(numero)}")
numero = 12332546
print(f"A soma do número {numero} é {soma_inteiros(numero)}")
numero = 23124546478
print(f"A soma do número {numero} é {soma_inteiros(numero)}")