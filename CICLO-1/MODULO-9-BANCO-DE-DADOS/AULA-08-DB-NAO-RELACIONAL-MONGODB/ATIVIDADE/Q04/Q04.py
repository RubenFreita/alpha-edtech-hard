from pymongo import MongoClient, ASCENDING


def adicionando_indice(
    nome_cliente,
    nome_colecao,
    campo_indice,
    tipo_indice,
):

    try:
        cliente = MongoClient("mongodb://localhost:27017/")

        db = cliente[nome_cliente]

        colecao = db[nome_colecao]
        colecao.create_index([(campo_indice, tipo_indice)])

    except Exception as e:
        print(e)


adicionando_indice(
    nome_cliente="atividade_1",
    nome_colecao="alunos",
    campo_indice="idade",
    tipo_indice=ASCENDING,
)
