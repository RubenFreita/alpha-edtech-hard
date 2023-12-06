#Questão 06

"""
ENTRADA: UM NÚMERO NATURAL N
SAÍDA: N! E QUANTOS ZEROS N! TEM.
"""



entrada = int(input("O fatorial de qual número você quer ver? "))

r = 1

for i in range(1, entrada+1):
    r *= i
count = 0
aux = r
for i in range(r):
    if aux%10 == 0:
        count += 1
        aux = aux//10
    else:
        break
print(f"O fatorial de {entrada} = {r}.")
print(f"O número {r} tem {count} zeros.")