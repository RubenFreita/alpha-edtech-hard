#Questão 07

"""
ENTRADA: UM NÚMERO NATURAL N
SAÍDA: INFORMA SE O NÚMERO N É PRIMO OU NÃO
"""


entrada = int(input("Qual número você quer verificar se é primo? "))
count = 0
for i in range(1,entrada+1):
    if entrada % i ==0:
        count += 1

if count == 2:
    print(f"O número {entrada} é primo")
else:
    print(f"O número {entrada} não é primo")
