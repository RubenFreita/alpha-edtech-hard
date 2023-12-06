#Questão 04

"""
ENTRADA: UM NÚMERO NATURAL A E UM NÚMERO INTEIRO B
SAÍDA: A^B
"""


base = int(input("Informe o número base: "))
expoente = int(input("Informe o número que será o expoente: "))
r = 1

for i in range(1,abs(expoente)+1):
    r *= base
if expoente < 0:
    r = 1/r

print(f"O resultado da operação {base}^{expoente} = {r}")