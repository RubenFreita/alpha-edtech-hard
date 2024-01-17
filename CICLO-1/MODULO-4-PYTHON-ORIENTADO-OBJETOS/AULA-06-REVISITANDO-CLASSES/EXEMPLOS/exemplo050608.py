import random


class Aluno:
    nota:float

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}, {self.idade} anos."


""" Tabela de alunos """
alunos = [
"Andre Henrique Gloos Ribeiro",
"Artur Matos Malcher De Sousa",
"ATHILIO ANTONIO CAVALCANTI RIBEIRO DA SILVA",
"Bianca Yuri de Almeida Waki",
"CARLOS AUGUSTO MOURA PIRES",
"YASMIM FERREIRA DOS SANTOS"
]

idade = []
for i, aluno in enumerate(alunos):
    idade.append(random.randint(17,25))
    print(alunos[i], idade[i])

alunosList = []
for _, aluno in enumerate(alunos):
    alunosList.append( Aluno (alunos[_], idade[_]) )

for _, alunoObjeto in enumerate(alunosList):
    print(alunoObjeto)

for _i, alunoObjeto in enumerate(alunosList):
    alunosList[_i].nota = float(input("Digite a nota de " + alunoObjeto.nome + ":= " ))

mediaNota = 0.0
for _, alunoObjeto in enumerate(alunosList):
    print("Nota de", alunosList[_].nome,  alunosList[_].nota)
    mediaNota += alunosList[_].nota
mediaNota = round(mediaNota/len(alunosList), 1)
print("Média Geral", mediaNota)
