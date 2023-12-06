#Questão 03

"""
ENTRADA: UM NÚMERO N DE 0 A 10
SAÍDA: A TABUADA DE NÚMERO N.
"""


entrada = int(input("Digite o número de 0 a 10 no qual deseja ver a tabuada: "))
if 0 <= entrada <= 10:
    print(f"Tabuada de {entrada}")


    for i in range(1,11):
        print(f"{i} X {entrada} = {entrada*i}")
else:
    print(f"O número {entrada} não está dentro do range de 0 a 10!")