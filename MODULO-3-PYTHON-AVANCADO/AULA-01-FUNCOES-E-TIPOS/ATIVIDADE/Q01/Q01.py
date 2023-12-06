import random

def boas_vindas():
    print("Bem-vindo(a) ao curso de Python!")


def aluno(nome, idade=18):
    if idade >= 18:
        boas_vindas()
        print(f"Aluno: {nome}")
        print(f"Idade: {idade}")
        print("Cadastro Efetivado!")
    else:
        print("Cadastro Não Efetivado!")
        print("Aluno é menor de idade!")

def cadastro_aluno(nome, idade, endereco, cep):
    matricula = ""
    for i in range(6):
        matricula += str(random.randint(0,9))
    turma = random.randint(1,5)

    return turma, matricula

nome_aluno1, idade_aluno1 = "José da Silva", 18
nome_aluno2 = "Ana Moreira"

aluno(nome_aluno1, idade_aluno1)
aluno(nome_aluno2)

print() 
nome_aluno3 = "José da Silva"
idade_aluno3 = 18
endereco_aluno3 = "Avenida Brasil, 100"
cep_aluno3 = "12345-789"

turma_aluno3, matricula_aluno3 = cadastro_aluno(nome_aluno3, idade_aluno3, endereco_aluno3, cep_aluno3)

print(f"Olá {nome_aluno3}, sua matrícula é Nº {matricula_aluno3}  na turma {turma_aluno3}.")