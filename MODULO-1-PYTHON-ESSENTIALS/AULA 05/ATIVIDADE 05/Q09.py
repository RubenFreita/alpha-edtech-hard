#Questão 09

"""
ENTRADA: UM NÚMERO N QUE IRÁ DEFINIR O TOTAL DE ALUNOS E EM SEGUIDA SERÁ INFORMADO N VEZES
O SEU CÓDIGO, A SUA ALTURA E O SEU PESO.
SAÍDA: SERÁ INDICADO PELO PROGRAMA  ALTURA DO MENOR E DO MAIOR ALUNO, 
O PESO DO ALUNO MAIS MAGRO E DO ALUNO MAIS GORDO, TODAS ELAS JUNTAMENTE COM SEUS 
RESPECTIVOS CÓDIGOS DE INDENTIFICAÇÃO. SERÁ INFORMADO TAMBÉM A MÉDIA DOS PESOS E
DAS ALTURAS DOS ALUNOS.
"""



quantidadeAlunos = int(input("Digite a quantidade de alunos: "))

menorAltura = None
maiorAltura = None
maiorPeso = None
menorPeso = None
somaPeso = 0
somaAltura = 0
for i in range(quantidadeAlunos):
    numeroAluno = int(input(f"Digite o código do aluno: "))
    alturaAluno = float(input(f"Digite a altura(em metros) do aluno {numeroAluno}: ").replace(",","."))
    pesoAluno = float(input(f"Digite o peso(em Kg) do aluno {numeroAluno}: ").replace(",","."))
    somaAltura += alturaAluno
    somaPeso += pesoAluno
    if  maiorAltura == None or alturaAluno > maiorAltura:
        maiorAltura = alturaAluno
        indiceMaiorAltura = numeroAluno
    if  menorAltura == None or alturaAluno < menorAltura:
        menorAltura = alturaAluno
        indiceMenorAltura = numeroAluno
    if  maiorPeso == None or pesoAluno > maiorPeso:
        maiorPeso = pesoAluno
        indiceMaiorPeso = numeroAluno
    if  menorPeso == None or pesoAluno < menorPeso:
        menorPeso = pesoAluno
        indiceMenorPeso = numeroAluno
mediaPeso = somaPeso/quantidadeAlunos
mediaAltura = somaAltura/quantidadeAlunos
print(f"O aluno mais alto é o aluno {indiceMaiorAltura} e tem altura {maiorAltura:.2f} M")
print(f"O aluno mais baixo é o aluno  {indiceMenorAltura} e tem altura {menorAltura:.2f} M")
print(f"O aluno mais gordo é o aluno  {indiceMaiorPeso} e tem peso {maiorPeso:.2f} Kg")
print(f"O aluno mais magro é o aluno  {indiceMenorPeso} e tem peso {menorPeso:.2f} Kg")
print(f"A média da altura dentre os alunos informados é: {mediaAltura:.2f} M")
print(f"A média do Peso dentre os alunos informados é: {mediaPeso:.2f} Kg")