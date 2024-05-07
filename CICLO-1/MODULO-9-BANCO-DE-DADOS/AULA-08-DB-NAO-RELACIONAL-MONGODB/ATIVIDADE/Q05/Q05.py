from pymongo import MongoClient


from pymongo import MongoClient, ASCENDING


def deletando_documentos(
    nome_cliente,
    nome_colecao,
    idade,
):

    try:
        cliente = MongoClient("mongodb://localhost:27017/")

        db = cliente[nome_cliente]

        colecao = db[nome_colecao]

        colecao.delete_many({"idade": {"$lt": idade}})

    except Exception as e:
        print(e)


deletando_documentos(
    nome_cliente="atividade_1",
    nome_colecao="alunos",
    idade=18,
)
