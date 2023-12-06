#Questão 02

"""
ENTRADA: UM NÚMERO N
SAÍDA: OS MÚLTIPLOS DE N DE 1 A 50.
"""

entrada = int(input("Digite um número: "))
print(f"Os múltiplos de {entrada} de 1 a 50 são: ", end="")
for i in range(1, 51):
    if i % entrada == 0:
        if i+entrada <=50:
            print(f"{i}", end=", ")
        else:
            print(f"{i}.")

