#Questão 10


"""
ENTRADA: O NÚMERO N QUE INDICA O NÚMERO DE ELEITORES 
E EM SEGUIDA O VOTO DE CADA ELEITOR NOS CANDIDATOS 1, 2 E 3
SÁIDA: O NÚMERO DE VOTOS PARA CADA CANDIDATO.
"""


candidato1 = 0
candidato2 = 0
candidato3 = 0

print("Seja bem vindo a Eleição!")
qtdEleitores = int(input("Informe a quantidade de eleitores: "))

for i in range(qtdEleitores):
    print("Digite 1 para votar no Candidato 1")
    print("Digite 2 para votar no Candidato 2")
    print("Digite 3 para votar no Candidato 3")
    voto = input("Informe seu voto: ")
    if voto == "1":
        candidato1 += 1 
    elif voto == "2":
        candidato2 += 1 
    elif voto == "3":
        candidato3 += 1
    else:
        print("Voto inválido!")

print(f"O candidato 1 teve {candidato1} votos")
print(f"O candidato 2 teve {candidato2} votos")
print(f"O candidato 3 teve {candidato3} votos")