#MODULO PARA A QUESTÃO 4
"""
ENTRADA: UM NÚMERO NATURAL N
SAÍDA: OS NÚMEROS PRIMOS DE 1 ATÉ N
"""


# entrada = int(input("Qual número você quer verificar se é primo? "))
def primo(numero):
    count = 0
    print(f"A lista dos números primos de 1 até {numero} é:")
    for j in range(1, numero+1):
        for i in range(1,j+1):
            if j % i == 0:
                count += 1

        if count == 2:
            print(f"{j}", end=", ")
        count = 0