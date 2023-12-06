#Questão 01


"""
ENTRADA: 5 NÚMEROS N
SAÍDA: O MAIOR, A SOMA E A MÉDIA DENTRE OS 5 NÚMEROS INFORAMDOS
"""

maior = 0
soma = 0
media = 0

maior = float(input("Digite um número: "))
soma = maior
for i in range(4):
    entrada = float(input("Digite um número: "))
    if entrada > maior:
        maior = entrada
    soma += entrada
media = soma / 5

print(f"A soma dos números informados é: {soma}")
print(f"A média dos números informados é: {media}")
print(f"O maior número dentre os informador é: {maior}")
