#Questão 08

"""
ENTRADA: 10 NÚMEROS N E A INDICANDO O NÚMERO DO ALUNO E A SUA ALTURA, RESPECTIVAMENTE
SAÍDA: O MAIOR E O MENOR ALUNO JUNTAMENTE COM SEU NÚMERO E SUA ALTURA.
"""


menor = None
maior = None
for i in range(1,4):
    numeroAluno = int(input(f"Digite o número do aluno: "))
    alturaAluno = float(input(f"Digite a altura(em metros) do aluno {numeroAluno}: ").replace(",","."))
    if  maior == None or alturaAluno > maior:
        maior = alturaAluno
        indiceMaior = numeroAluno
    if  menor == None or alturaAluno < menor:
        menor = alturaAluno
        indiceMenor = numeroAluno
print(f"O maior aluno é o número {indiceMaior} e tem altura {maior:.2f}")
print(f"O menor aluno é o número {indiceMenor} e tem altura {menor:.2f}")