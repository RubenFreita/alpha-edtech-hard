import random


# Definindo a classe Endereco
class Endereco:
    def __init__(self, rua, cidade, estado):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return f"{self.rua}, {self.cidade}, {self.estado}"


class Aluno:
    nota:float
    enderCobr: Endereco

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

endereco1 = Endereco("Av Barao do Rio Branco", "Angra dos Reis", "RJ")
endereco2 = Endereco("Rua Bela Vista", "Bonito", "MS")
endereco3 = Endereco("Rua Central", "Recife", "PE")

for _, alunoObjeto in enumerate(alunosList):
    print(alunoObjeto)

for _i, alunoObjeto in enumerate(alunosList):
    alunosList[_i].nota = float(input("Digite a nota de " + alunoObjeto.nome + ":= " ))
    if _i % 3 == 0:
        alunosList[_i].enderCobr = endereco1
    elif _i % 3 == 1:
        alunosList[_i].enderCobr = endereco2
    else:
        alunosList[_i].enderCobr = endereco3
    
mediaNota = 0.0
for _, alunoObjeto in enumerate(alunosList):
    print("Nota de", alunosList[_].nome,  alunosList[_].nota, "morador", alunosList[_].enderCobr)
    mediaNota += alunosList[_].nota
mediaNota = round(mediaNota/len(alunosList), 1)
print("Média Geral", mediaNota)
