import random


class Aluno:
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
"CLEVERSON GUANDALIN",
"DEIVID FERNANDO DA SILVA",
"Diego Alvarenga Rodrigues",
"DJULLIE CAROLINE DE BARROS ROCHA",
"ELIAS DAVID OLIVEIRA SOUSA",
"EWERTON SOUZA PEREIRA",
"FELIPHE CRUZ DE LIMA",
"FERNANDO SANTOS MORENO",
"FRANCISCO RUBEN VASCONCELOS FREITAS",
"GABRIEL DA SILVA FERREIRA",
"Gabriel Freire De Almeida Vitorino",
"GUILHERME DUARTE BARCELOS",
"IGOR SOUZA",
"INGRID ROCHA DE SOUSA",
"JOAO PEDRO RAMOS FAUSTINO PEREIRA MARQUES",
"Joao Victor Sena Salomao",
"JOSE MARIO DA SILVA JUNIOR",
"JOSE MIGUEL CLAUDINO RAMALHO",
"Kennendh Anderson da Silva",
"LUAN HENRRY VIDAL OLIVEIRA",
"LUCAS DIEGO SANTOS DA SILVA",
"LUIS CARLOS DA SILVA BEZERRA",
"Magno Evangelista",
"Renan Rigolon Coelho Pinto",
"Taynara De Morais Pereira",
"Tiago Monteiro Dos Santos Souza",
"Victor Martins",
"YASMIM FERREIRA DOS SANTOS"
]

idade = []
for i, aluno in enumerate(alunos):
    idade.append(random.randint(17,25))
    print(alunos[i], idade[i])

alunosList = []
for _ in range(len(alunos)):
    alunosList.append( (alunos[_], idade[_]) )

for _ in range(len(alunos)):
    print( alunosList[_])
