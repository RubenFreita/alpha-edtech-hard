"""
ENTRADA: UM NÚMERO NATURAL N
SAÍDA: INFORMA SE O NÚMERO N É PRIMO OU NÃO
"""


entrada = int(input("Informe um número inteiro: "))
count = 0
i = 1
aux = 0
for j in range(1,entrada+1):
    i = 1
    count = 0
    while i <= j:
        aux += 1
        if j % i == 0:
            count += 1
        if count > 2:
            break
        i += 1
    
    if count == 2:
        print(f"{j}", end=", ")
print()
print(f"O programa executou {aux} divisões para encontrar todos os números primos entre 1 e {entrada}")