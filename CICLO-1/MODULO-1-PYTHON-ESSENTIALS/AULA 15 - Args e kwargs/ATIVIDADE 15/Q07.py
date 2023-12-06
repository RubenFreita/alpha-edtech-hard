

def verifica_media(media):
    if media > 7:
        return "Aprovado"
    return "Reprovado"

#situação para um aluno apenas
def situacao_aluno(aluno, media):
    return {aluno: verifica_media(media)}

#situação para varios alunos
def situacao_alunos(**relacao_alunos):
    return {"situação_alunos":[situacao_aluno(aluno, media) for aluno, media in relacao_alunos.items()]}

print(situacao_aluno("Artur", 7.1))
print(situacao_alunos(ruben=9, joao=7, maria=10))